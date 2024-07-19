import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

#https://www.pro-football-reference.com/about/win_prob.htm
#time_lef in min
#vegas_line is spread i believe
def home_win_prob(away_margin, time_left, home_vegas_line):
	#https://stackoverflow.com/questions/59012763/how-to-calculate-cumulative-normal-distribution-in-python
	#1-stats.norm.cdf(x, mean, sigma)

	std = 13.5

	one = 1 - stats.norm.cdf((away_margin + 0.5), 
			(-home_vegas_line * (time_left / 60)),
			(std/np.sqrt(60 / time_left)))
	two = 0.5 * stats.norm.cdf((away_margin + 0.5), 
			(-home_vegas_line * (time_left / 60)),
			(std/np.sqrt(60 / time_left)))
	three = stats.norm.cdf(away_margin - 0.5,
			(-home_vegas_line * (time_left / 60)),
			(std/np.sqrt(60 / time_left)))

	return one + two - three

db = pd.read_csv("../data/play_by_play_2023.csv")

#print(home_win_prob(7 - 10 + 0.13, 1874/60, -3))
#exit()

clean = db[['home_team', 'away_team', 'total_home_score', 
	    'total_away_score', 'yrdln', 'posteam', 'ydstogo', 'down',
            'game_seconds_remaining', 'time', 'ep', 'epa']]

#https://www.espn.com/nfl/game/_/gameId/401547646/broncos-raiders
clean = clean[clean['home_team'] == 'LV']
clean = clean[clean['away_team'] == 'DEN']

clean = clean.reset_index()

game_list = [] 

for index, row in clean.iterrows():
	curr = {}
	curr['home_team'] = row['home_team']
	curr['away_team'] = row['away_team']
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

for item in game_list:
	win_prob = 0
	try:		
		if item['possession'] == item['away_team']:
			win_prob = home_win_prob((item['away_score'] + item['ep']) 
				 - item['home_score'], item['game_sec_remain'] / 60, -3.5)
		else:
			win_prob = home_win_prob(item['away_score'] - (item['home_score'] 
				+ item['ep']), item['game_sec_remain'] / 60, -3.5)
		item['win_prob'] = win_prob
	except: 
		print("OVER")

for idx, item in enumerate(game_list): 
	try:
		item['win_added'] = abs(game_list[idx + 1]['win_prob'] - game_list[idx]['win_prob'])
	except:
		item['win_added'] = 0
		print("OUT")

sorted_list = sorted(game_list, key=lambda d: d['win_added'], reverse=True)

for i in range(0, 10):
	print(sorted_list[i])
