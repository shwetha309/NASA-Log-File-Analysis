from file_write import format_data
from datetime import datetime, timedelta

def get_block_list(row, flogin_host_dict, block_list, block_hosts_dict):
	''' 
	Description: Feature 4 processing by considering the various input cases
	Input: Input row, Dictionary to maintain host as key and value as a list of (counter, Entry Timestamp, End of 20 second timestamp, Blocking Start Timestamp, Blocking End Timestamp)
	Output: None
	'''
	host=row[0]
	curr_ts=row[1]
	request=row[2]
	httpcode=row[3]
	byte=row[4]

	if host in flogin_host_dict:
				
			
		dict_row=flogin_host_dict[host]
		ctr=dict_row[0]
		entry_ts=dict_row[1]
		end_20s_ts=dict_row[2]
		block_start_ts=dict_row[3]
		block_end_ts=dict_row[4]
	
		if httpcode=="200":
			
				
			### Case 1: Valid Login Attempt after end of block period 
			### Remove the host name from Failed Login dictionary
			if block_end_ts is not None and curr_ts >= block_end_ts:	#???
				flogin_host_dict.pop(host,None)

			### Case 2: If counter is 3 and Valid Login Attempt during block period
			### Make an entry in the blocked list
			elif block_end_ts is not None and block_start_ts is not None:
				if curr_ts >=block_start_ts and curr_ts<block_end_ts:	#???
					out_data=format_data(host,curr_ts,request, httpcode,byte)
					block_list.append(out_data)

			### Case 3: Valid Login attempt before end of 20s grace period
			### Remove the host name from Failed Login dictionary
			elif "login" in request and curr_ts < end_20s_ts:	#???
				flogin_host_dict.pop(host)

			

				

		### For all other response codes:
		elif httpcode !="200":  							
				
			### Case 1: If counter is 3 and Invalid Login Attempt during block period
			### Make an entry in the blocked list
			if block_end_ts is not None and block_start_ts is not None:
				if curr_ts >=block_start_ts and curr_ts<block_end_ts:	#???
					out_data=format_data(host,curr_ts,request, httpcode,byte)
					block_list.append(out_data)
			
			#### Case 2: Failed Login Attempt #2
			elif curr_ts<= end_20s_ts and "login" in request:
				if ctr==1:
					flogin_host_dict[host]=[2,entry_ts,end_20s_ts,block_start_ts,block_end_ts]

				#### Case 2: Failed Login Attempt #2, set the block periods
				elif ctr==2 and "login" in request:
					flogin_host_dict[host]=[3,entry_ts,end_20s_ts,curr_ts,curr_ts+timedelta(seconds=301)]
					
					if host in block_hosts_dict:
						block_hosts_dict[host] = block_hosts_dict[host]+1
					else:
						block_hosts_dict[host] = 1
			
			### Case 3: Failed Login but after 20s time, reset the values
			elif ctr <3 and curr_ts >= dict_row[2] and "login" in request:		#???
				flogin_host_dict[host]=[1,curr_ts,curr_ts+timedelta(seconds=20),None,None]
			
				
	else:

		if httpcode =="401" and "login" in request:
			flogin_host_dict[host]=[1,curr_ts,curr_ts+timedelta(seconds=20),None,None]

	
