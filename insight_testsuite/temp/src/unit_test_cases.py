import pandas as pd 
import time, re, sys, unittest
from datetime import datetime, timedelta

from file_write import file_write
from blocked_list import get_block_list
from resources import get_resources_list
from hosts import get_hosts_list
from busy_hours import get_busy_period


data=[["212.148.61.74",pd.to_datetime("04/Jul/1995:03:39:52", format='%d/%b/%Y:%H:%M:%S'),"GET /login HTTP/1.0","401",int(7074)],["212.148.61.74",pd.to_datetime("04/Jul/1995:03:39:52", format='%d/%b/%Y:%H:%M:%S'),"GET /login HTTP/1.0","401",int(7074)],["212.148.61.74",pd.to_datetime("04/Jul/1995:03:39:52", format='%d/%b/%Y:%H:%M:%S'),"GET /login HTTP/1.0","401",int(7074)],["212.148.61.74",pd.to_datetime("04/Jul/1995:03:39:52", format='%d/%b/%Y:%H:%M:%S'),"GET /login HTTP/1.0","200",int(7074)]]

empty_list=[]

def get_Size_list(data):
	flogin_host_dict={}
	block_hosts_dict={}
	block_list=[]
	get_block_list(data, flogin_host_dict, block_list, block_hosts_dict)
	return len(block_list)

def check_block(data):
	flogin_host_dict={}
	block_hosts_dict={}
	block_list=[]
	for i in range(0,len(data)):
		
		get_block_list(data[i], flogin_host_dict, block_list, block_hosts_dict)
		
	return len(block_list)

def get_resources_sum(data):
	resources_dict={}
	for i in range(0,len(data)):
		get_resources_list(data[i], resources_dict)
	resources_list=sorted(resources_dict.items(), key=lambda x:(-x[1]))
	bandwidth=0
	for i in range(0,len(resources_list)):
		bandwidth=bandwidth+resources_list[i][1]
	return bandwidth

def get_top_host(data):
	if len(data)==0:
		return None
	host_dict={}
	for i in range(0,len(data)):
		print data[i]
		get_hosts_list(data[i], host_dict)
	hosts_list=sorted(host_dict.items(), key=lambda x:(-x[1]))

	return hosts_list[0][0]

def get_hours(data):
	if len(data) == 0:
		return None
	df=pd.DataFrame(data,columns=['host','timestamp','request','http reply code','bytes'])
	df_ts_grp=df.groupby('timestamp')['timestamp'].count().sortlevel(0,1)
	busy_hours_list=get_busy_period(df_ts_grp)
	return busy_hours_list[0][0]

class blocked_list_Tests(unittest.TestCase):		

    def test_block_list(self):
    	self.assertEqual(get_Size_list(data[-1]),0)

    def test_block_list_2(self):
    	self.assertEqual(check_block(data),1)

class resouces_list_Tests(unittest.TestCase):		

    def test_resources_list (self):
    	self.assertEqual(get_resources_sum(empty_list),0)

    def test_resources_sum (self):
    	self.assertEqual(get_resources_sum(data),28296)

class hosts_list_Tests(unittest.TestCase):		

    def test_host_1 (self):
    	self.assertEqual(get_top_host(empty_list),None)

    def test_host_2 (self):
    	self.assertEqual(get_top_host(data),"212.148.61.74")

class hours_list_Tests(unittest.TestCase):		

    def test_hours_1 (self):
    	self.assertEqual(get_hours(empty_list),None)

    def test_hours_2 (self):
    	self.assertEqual(get_hours(data),pd.to_datetime("04/Jul/1995:03:39:52", format='%d/%b/%Y:%H:%M:%S'))





def main():
    unittest.main()

if __name__ == '__main__':
    main()