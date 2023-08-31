from flask import Flask, render_template,redirect, url_for

app = Flask(__name__)

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

if __name__ == "__main__":
    app.run(debug = True)


