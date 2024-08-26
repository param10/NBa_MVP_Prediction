Overview

This project focuses on predicting NBA MVP (Most Valuable Player) shares using machine learning models. The project includes scraping data from the Basketball Reference website, cleaning the data, and then using it to train models for prediction.

Usage

	1.	Data Scraping: Use the 1_data_scraping.ipynb notebook to collect data from the Basketball Reference website.
	2.	Data Cleaning: Use the 2_cleaning_analysis.ipynb notebook to clean and prepare the data for analysis.
	3.	Modeling: Use the 3_modeling.ipynb notebook to train machine learning models and make predictions on MVP shares.

Features

	•	Scrape NBA data for MVPs, players, and teams.
	•	Clean and process the data.
	•	Train models to predict MVP shares.

Data Description

1. MVP Data 

	•	Rank: Player’s rank in MVP voting for that year.
	•	Player: Name of the player.
	•	Age: Age of the player during the season.
	•	Tm: Team abbreviation.
	•	First: Number of first-place votes received.
	•	Pts Won: Total MVP points won by the player.
	•	Pts Max: Maximum possible MVP points.
	•	Share: Percentage share of MVP points (Pts Won / Pts Max).
	•	G: Games played.
	•	MP: Minutes played per game.
	•	PTS: Points per game.
	•	TRB: Total rebounds per game.
	•	AST: Assists per game.
	•	STL: Steals per game.
	•	BLK: Blocks per game.
	•	FG%: Field goal percentage.
	•	3P%: Three-point percentage.
	•	FT%: Free throw percentage.
	•	WS: Win Shares (an estimate of the number of wins contributed by the player).
	•	WS/48: Win Shares per 48 minutes.
	•	Year: The NBA season year.

2. Player Data 

	•	Player: Name of the player.
	•	Pos: Position of the player (e.g., SG, PF).
	•	Age: Age of the player during the season.
	•	Tm: Team abbreviation.
	•	G: Games played.
	•	GS: Games started.
	•	MP: Minutes played per game.
	•	FG: Field goals made per game.
	•	FGA: Field goals attempted per game.
	•	FG%: Field goal percentage.
	•	3P: Three-point field goals made per game.
	•	3PA: Three-point field goals attempted per game.
	•	3P%: Three-point percentage.
	•	2P: Two-point field goals made per game.
	•	2PA: Two-point field goals attempted per game.
	•	2P%: Two-point percentage.
	•	eFG%: Effective field goal percentage (accounts for the fact that a 3-point field goal is worth more than a 2-point field goal).
	•	FT: Free throws made per game.
	•	FTA: Free throws attempted per game.
	•	FT%: Free throw percentage.
	•	ORB: Offensive rebounds per game.
	•	DRB: Defensive rebounds per game.
	•	TRB: Total rebounds per game.
	•	AST: Assists per game.
	•	STL: Steals per game.
	•	BLK: Blocks per game.
	•	TOV: Turnovers per game.
	•	PF: Personal fouls per game.
	•	PTS: Points scored per game.
	•	Year: The NBA season year.

3. Team Data 

	•	Team: Name of the team.
	•	W: Number of wins during the season.
	•	L: Number of losses during the season.
	•	W/L%: Win/Loss percentage.
	•	GB: Games behind (relative to the first place).
	•	PS/G: Points scored per game by the team.
	•	PA/G: Points allowed per game by the team.
	•	SRS: Simple Rating System, a rating that takes into account average point differential and strength of schedule.
	•	Year: The NBA season year.

License

This project is licensed under the MIT License. See the LICENSE file for more details.

This version is more straightforward and easier to follow, with just the essential information. Let me know if this works for you or if there’s anything else you’d like to adjust!
