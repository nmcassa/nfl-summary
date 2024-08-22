import math

#TODO: WINNING TEAM BIAS
def add_biases(plays):
	for idx, item in enumerate(plays):
		if item['desc'][0] != '(':
			plays[idx]['win_added'] = 0
		if not math.isnan(item['yards_gained']):
			plays[idx]['win_added'] += (abs(item['yards_gained'] / 500))
	return plays
