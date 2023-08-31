from flask import Flask, render_template, request, flash, redirect, url_for
import pickle
import pandas as pd

app = Flask(__name__)
app.secret_key = 'some_secret_key'  # Required for flashing messages

@app.route('/')
def root():
    return redirect(url_for('homepage'))

@app.route('/homepage')
def homepage():
    fields = [
        {"id": "name", "label": "Player Name", "type": "text", "placeholder": "Enter name"},
        {"id": "Age", "label": "Age", "type": "number", "placeholder": "Prime age (e.g., 25)"},
        {"id": "G", "label": "Games Played", "type": "number", "placeholder": "Played all Games (e.g., 82)"},
        {"id": "GS", "label": "Games Started", "type": "number", "placeholder": "Started all Games (e.g., 82)"},
        {"id": "MP", "label": "Minutes Per Game", "type": "number", "placeholder": "High Minutes Per Game (e.g., 40.0)"},
        {"id": "FG", "label": "Field Goals Made", "type": "number", "placeholder": "High Field Goals Made (e.g., 24.0)"},
        {"id": "FGA", "label": "Field Goals Attempted", "type": "number", "placeholder": "Efficient Shooting (e.g., 23.0)"},
        {"id": "3P", "label": "Three-Point Field Goals Made", "type": "number", "placeholder": "Elite 3-point Shooter (e.g., 9.0)"},
        {"id": "3PA", "label": "Three-Point Field Goals Attempted", "type": "number", "placeholder": "Good 3-point Attempts (e.g., 10.0)"},
        {"id": "2P", "label": "Two-Point Field Goals Made", "type": "number", "placeholder": "Good 2-point Field Goals Made (e.g., 9.0)"},
        {"id": "2PA", "label": "Two-Point Field Goals Attempted", "type": "number", "placeholder": "Efficient 2-point Shooting (e.g., 16.0)"},
        {"id": "FT", "label": "Free Throws Made", "type": "number", "placeholder": "High Free Throws Made (e.g., 10.0)"},
        {"id": "FTA", "label": "Free Throw Attempts", "type": "number", "placeholder": "High Free Throw Attempts (e.g., 12.0)"},
        {"id": "ORB", "label": "Offensive Rebounds", "type": "number", "placeholder": "Offensive Rebounds (e.g., 6)"},
        {"id": "DRB", "label": "Defensive Rebounds", "type": "number", "placeholder": "Defensive Rebounds (e.g., 15.0)"},
        {"id": "AST", "label": "Assists", "type": "number", "placeholder": "Elite Assists (e.g., 11.0)"},
        {"id": "STL", "label": "Steals", "type": "number", "placeholder": "Elite Steals (e.g., 2.5)"},
        {"id": "BLK", "label": "Blocks", "type": "number", "placeholder": "Good Blocks for a Guard/Forward (e.g., 6)"},
        {"id": "TOV", "label": "Turnovers", "type": "number", "placeholder": "Low Turnovers (e.g., 1.0)"},
        {"id": "PF", "label": "Personal Fouls", "type": "number", "placeholder": "Low Personal Fouls (e.g., 1.0)"},
        {"id": "Year", "label": "Year", "type": "number", "placeholder": "Year (e.g., 2021)"},
        {"id": "W", "label": "Wins", "type": "number", "placeholder": "Team Won a Lot of Games (e.g., 70)"},
        {"id": "L", "label": "Losses", "type": "number", "placeholder": "Few Losses (e.g., 12)"},
        {"id": "GB", "label": "Games Behind", "type": "number", "placeholder": "Close to Top Seed (e.g., 1)"},
        {"id": "PS/G", "label": "Points Scored Per Game", "type": "number", "placeholder": "Team's High Points per Game (e.g., 120.0)"},
        {"id": "PA/G", "label": "Points Allowed Per Game", "type": "number", "placeholder": "Team's Low Points Allowed per Game (e.g., 100.0)"},
        {"id": "SRS", "label": "Simple Rating System", "type": "number", "placeholder": "High Simple Rating System (e.g., 10.0)"}
    ]

    return render_template('homepage.html', fields=fields)


@app.route('/predict', methods=['POST'])
def predict():
    # Load the model
    with open('/Users/paramjaswal/Desktop/NBa/neuralNetwork.pkl', 'rb') as model_file:
        model = pickle.load(model_file)
    

    # Extract data from form
    data = {key: float(request.form[key]) for key in request.form if key != "name"}
    player_name = request.form["name"]
    year = int(request.form["Year"])

    # Compute additional metrics based on the provided data
    data['FG%'] = data['FG'] / data['FGA']
    data['3P%'] = data['3P'] / data['3PA']
    data['2P%'] = data['2P'] / data['2PA']
    data['eFG%'] = (data['FG'] + 0.5 * data['3P']) / data['FGA']
    data['FT%'] = data['FT'] / data['FTA']
    data['TRB'] = data['ORB'] + data['DRB']
    data['PTS'] = data['FT'] + 2 * data['2P'] + 3 * data['3P']
    data['W/L%'] = data['W'] / (data['W'] + data['L'])

    # Extract relevant data from the main stats DataFrame based on the provided year
    stats = pd.read_csv("/Users/paramjaswal/Desktop/NBa/Player_mvp_stats.csv")
    data_for_year = stats[stats['Year'] == year]

    predictors = ['Age',  'G', 'GS', 'MP', 'FG', 'FGA', 'FG%', '3P',
       '3PA', '3P%', '2P', '2PA', '2P%', 'eFG%', 'FT', 'FTA', 'FT%', 'ORB',
       'DRB', 'TRB', 'AST', 'STL', 'BLK', 'TOV', 'PF', 'PTS', 'Year',
        'W', 'L', 'W/L%', 'GB', 'PS/G', 'PA/G', 'SRS']
    
    # Extract relevant columns from data_for_year
    data_for_year_relevant = data_for_year[predictors]

    # Ensure that player_data only contains the predictors columns
    player_data = pd.DataFrame([data], columns=predictors)

    # Concatenate the player_data with the relevant data_for_year columns
    data_for_prediction = pd.concat([data_for_year_relevant, player_data], ignore_index=True)


    # Predict MVP share for all players including the hypothetical player
    predictions = model.predict(data_for_prediction)

    # Create the final DataFrame with player names and their predicted MVP share
    player_names = data_for_year['Player'].tolist() + [player_name]
    result_df = pd.DataFrame({
        'Player': player_names,
        'Predicted MVP Share': predictions
    })

    # Sort players based on predicted MVP share
    sorted_df = result_df.sort_values(by="Predicted MVP Share", ascending=False).reset_index(drop=True)

    # Display top ten predictions
    top_ten = sorted_df.head(10)
    for index, row in top_ten.iterrows():
        flash(f"Rank {index + 1}: {row['Player']} with MVP Share of {row['Predicted MVP Share']:.2f}")
    top_ten = sorted_df.head(10)
    messages = []
    for index, row in top_ten.iterrows():
        messages.append(f"Rank {index + 1}: {row['Player']} with MVP Share of {row['Predicted MVP Share']:.2f}")
        
    return render_template('predict.html', messages=messages)



if __name__ == "__main__":
    app.run(debug=True)







