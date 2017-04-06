import pandas as pd 
from datetime import datetime , timedelta


''' Description: Gets the busiest 60 minute interval by using Pandas Dataframe, memoization and implementing Priority Queues for lists
	Input: Pandas Grouped Time Frame Obejct
	Output: Top 10 Timestamps'''

def get_busy_period(ts_df):

	start_ts=ts_df.index[0]
	end_ts=ts_df.index[len(ts_df)-1]
	#print end_ts

	### Getting count of items between start and end timestamp
	curr_end_ts=start_ts+timedelta(seconds=3599)
	curr_count=ts_df[start_ts:curr_end_ts].sum()
		
	### Implemented Priority Queues for two tuples
	heap=[]
	#heapq.heapify(heap)
	#heapq.heappush(heap,(curr_count,start_ts))
	heap.append([start_ts,curr_count])

	while(start_ts<=end_ts):
		
		if start_ts in ts_df.index:
			curr_count=curr_count-(ts_df[start_ts].sum())

		### Using Memoization
		start_ts=start_ts+timedelta(seconds=1)
		next_ts=start_ts+timedelta(seconds=3599)

		if (next_ts in ts_df.index):
			curr_count=curr_count+(ts_df[next_ts].sum())

		### Popping the smaller element
		
		heap.append([start_ts,curr_count])
		if len(heap)>10:
			heap = heap_pop(heap)

	newlist = sorted(heap, key=lambda x: (-x[1], x[0]))
	return newlist


### Popping the smallest element in heap for two column lists using lambda functions
def heap_pop(heap):
	newlist = sorted(heap, key=lambda x: (-x[1], x[0]))
	newlist.pop()
	return newlist