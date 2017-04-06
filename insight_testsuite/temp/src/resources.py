import pandas as pd

def get_url(request_str):
	request=request_str.replace("POST","").replace("HTTP/1.0","").replace("GET","").strip()
	return request

def get_resources_list(inp_row, resources_dict):

	request=inp_row[2]
	url=get_url(request)
	byte=inp_row[4]

	if url not in resources_dict:
		resources_dict[url]=int(byte)
	else:
		resources_dict[url]=resources_dict[url]+byte

def get_top_hits(inp_row,hit_page_dict):

	request=inp_row[2]
	url=get_url(request)

	if url in hit_page_dict:
		hit_page_dict[url]=hit_page_dict[url]+1
	else:
		hit_page_dict[url]=1


def get_failed_page(inp_row,failed_page_dict):
	
	request=inp_row[2]
	httpcode=inp_row[3]
	url=get_url(request)

	if httpcode != "200":
		if url in failed_page_dict:
			failed_page_dict[url]=failed_page_dict[url]+1
		else:
			failed_page_dict[url]=1
