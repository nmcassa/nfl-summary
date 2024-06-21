import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

db = pd.read_csv("../data/play_by_play_2023.csv")

clean = db[['home_team', 'away_team', 'total_home_score', 
	    'total_away_score', 'yrdln', 'posteam', 'ydstogo', 'down',
            'game_seconds_remaining', 'time', 'ep', 'epa']]

clean = clean[clean['home_team'] == 'LV']
clean = clean[clean['away_team'] == 'DEN']

clean = clean.reset_index()

game_list = [] 

for index, row in db.iterrows():
	curr = {}
	curr['home_score'] = row['total_home_score']
	curr['away_score'] = row['total_away_score']
	curr['yardline'] = row['yrdln']
	curr['possession'] = row['posteam']
	curr['yards_to_go'] = row['ydstogo']
	curr['down'] = row['down']
	curr['game_sec_remain'] = row['game_seconds_remaining']
	curr['time'] = row['time']
	curr['ep'] = row['ep']
	curr['epa'] = row['epa']
	game_list.append(curr)

print(game_list)
