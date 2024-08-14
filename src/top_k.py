# https://stackoverflow.com/questions/23418545/finding-top-k-elements-in-array-python-without-heapq-or-sorting

# ok this did not work
# not in order/chronological
def get_top_k(plays, k):
	ret = []

	# annoying but I want indexes to stay the same after pop
	# cpy = plays.copy()

	win_probs = []
	for item in plays:
		win_probs.append(item['win_added'])

	for i in range(k):
		pos = win_probs.index(max(win_probs))	
	#	ret.append(cpy[pos])
		ret.append(win_probs[pos])
	#	cpy.pop(pos)      
		win_probs.pop(pos)

	return ret
		
#chronological
def dumb_top_k(plays, k):
	last = min(get_top_k(plays, k))

	ret = []
	
	for item in plays:
		if item['win_added'] >= last:
			ret.append(item['desc'])
	
	return ret
