

### Formatting the Timestamp Object and formatting the output
def format_data(host,ts,url,httpcode,byte):
	datetime_obj=ts.to_pydatetime()
	outdata=host+" - - ["+str(datetime_obj.strftime("%d/%b/%Y:%H:%M:%S"))+" -0400] \""+url+"\" "+httpcode+" "+str(byte)
	return outdata


### Writing to a file
def file_write(wlist,wfile,feature_no):
	''' Input: List to write, File to write, Feature No
		Output: None '''
	
	if feature_no == 1:
		length=10
		if len(wlist)<10:
			length=len(wlist)

		for i in range(0,length):
			wfile.write(wlist[i][0]+","+str(wlist[i][1]))
			if i+1 != length:
				wfile.write("\n")

	elif feature_no == 2 or feature_no == 6 or feature_no == 7:
	
		length=10
		if len(wlist)<10:
			length=len(wlist)
		
		for i in range(0,length):
			wfile.write(wlist[i][0])
			if i+1 != length:
				wfile.write("\n")

	elif feature_no == 3:
		length=10
		if len(wlist)<10:
			length=len(wlist)
		#print "wlist", wlist
		for i in range(0,length):
			datetime_obj=wlist[i][0].to_pydatetime()
			ts=str(datetime_obj.strftime("%d/%b/%Y:%H:%M:%S"))+" -0400"
			wfile.write(ts+","+str(wlist[i][1]))
			if i+1 != length:
				wfile.write("\n")
	
	elif feature_no == 4:
		for i in range(0,len(wlist)):
			wfile.write(wlist[i])
			if i+1 != len(wlist):
				wfile.write("\n")

	elif feature_no == 5:
		length=10
		if len(wlist)<10:
			length=len(wlist)
		
		for i in range(0,length):
			wfile.write(wlist[i][0])
			if i+1 != length:
				wfile.write("\n")

	

