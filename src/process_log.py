import pandas as pd 
import time, re, sys
from datetime import datetime, timedelta

from file_write import file_write
from blocked_list import get_block_list
from resources import get_resources_list,get_top_hits,get_failed_page
from hosts import get_hosts_list
from busy_hours import get_busy_period

def generate_feature_hash_file(input_filename,feature_1_out_file,feature_2_out_file,feature_3_out_file,feature_4_out_file,feature_5_out_file,feature_6_out_file,feature_7_out_file):

	''' Description: Preprocesses Input File using regex, calls the functions corresponding to the features, and writes the received output

		Input: Input Filename, Feature 1- Feature 7 output file names
		Return : None
	'''

	### Initializing dictionaries and lists
	flogin_host_dict={}
	block_list=[]
	block_hosts_dict={}
	inp_rows=[]
	resources_dict={}
	host_dict={}
	hit_page_dict={}
	failed_page_dict={}

	### Open input file
	print "\nReading Input file and parsing it"
	with open(input_filename,'r') as file:
		for line in file:
			line=line.strip().replace("- -","&&&")	### Clears the whitespaces
			
			host_obj = re.search('[^&&&]*',line)	### Using regex to extract the content
			host=host_obj.group().strip()

			ts_obj = re.search('\[(.*?)\]',line)	### Using regex to extract the content
			ts=ts_obj.group().replace("[",'').replace("]",'').strip().split(' ')
			ts=pd.to_datetime(ts[0], format='%d/%b/%Y:%H:%M:%S')

			request_pat = re.search('"(.*?)"',line)	### Using regex to extract the content
			request=request_pat.group().replace("\"",'').strip()
			#url=get_url(request)

			final_part = line.split(' ')	
			httpcode = final_part[-2]		### httpcode value assigning

			if final_part[-1] =='-':
				byte=0
			else:
				byte=int(final_part[-1])	### bytecode value is assigned

			inp_row=[host,ts,request,httpcode,byte]	### Creating a list of input rows

			get_block_list(inp_row, flogin_host_dict, block_list, block_hosts_dict)	### Feature 4 & 5
			get_resources_list(inp_row, resources_dict)	### Feature 2
			get_hosts_list(inp_row,host_dict)	### Feature 1
			get_top_hits(inp_row,hit_page_dict)	### Feature 6
			get_failed_page(inp_row,failed_page_dict)	### Feature 7


			inp_rows.append([host,ts,request,httpcode,byte])
	
	### Sorting the output of the Features 1 and 2 and writing to a file
	hosts_list=sorted(host_dict.items(), key=lambda x:(-x[1],x[0]))		
	resources_list=sorted(resources_dict.items(), key=lambda x:(-x[1],x[0]))

	print "\n\nWriting ouputs of Features 1 and 2"
	file_write(hosts_list,open(feature_1_out_file,'w'),1)
	file_write(resources_list,open(feature_2_out_file,'w'),2)

	print "\n\nProcessing Feature 3"
	### Generating a Pandas DataFrame for Feature 3 and writing the output
	if len(inp_rows) > 0:
		df=pd.DataFrame(inp_rows,columns=['host','timestamp','request','http reply code','bytes'])
		df_ts_grp=df.groupby('timestamp')['timestamp'].count().sortlevel(0,1)
		busy_hours_list=get_busy_period(df_ts_grp)
		file_write(busy_hours_list,open(feature_3_out_file,'w'),3)

	print "\n\nWriting ouputs of Features 4,5,6,7"
	### Sorting the output of the Features 4,5,6,7 and writing to a file
	file_write(block_list,open(feature_4_out_file,'w'),4)
   	block_hosts_list=sorted(block_hosts_dict.items(), key=lambda x:(-x[1],x[0]))
   	file_write(block_hosts_list,open(feature_5_out_file,'w'),5)

   	top_hit_pages_list=sorted(hit_page_dict.items(), key=lambda x:(-x[1],x[0]))
	failed_page_list=sorted(failed_page_dict.items(), key=lambda x:(-x[1],x[0]))

	file_write(top_hit_pages_list,open(feature_6_out_file,'w'),6)
	file_write(failed_page_list,open(feature_7_out_file,'w'),7)



if __name__ == "__main__":

	### Main()
	### Getting Input and Output file names
	input_filename=sys.argv[1]
	feature_1_out_file=sys.argv[2]+"hosts.txt"
	feature_2_out_file=sys.argv[2]+"resources.txt"
	feature_3_out_file=sys.argv[2]+"hours.txt"
	feature_4_out_file=sys.argv[2]+"blocked.txt"
	feature_5_out_file=sys.argv[2]+"blocked_users.txt"
	feature_6_out_file=sys.argv[2]+"top_hit_pages.txt"
	feature_7_out_file=sys.argv[2]+"load_failed_pages.txt"

	print "Insight Coding Challenge 2017"
	start=time.time()
	print "Start Time = "+str(datetime.now())
	print "\n\nPreprocessing Input File"
	generate_feature_hash_file(input_filename,feature_1_out_file,feature_2_out_file, feature_3_out_file, feature_4_out_file, feature_5_out_file,feature_6_out_file,feature_7_out_file)
	
	print "\n\nTotal Time Taken ins seconds "+str(time.time()-start)
	print "\nEnd Time"+str(datetime.now())