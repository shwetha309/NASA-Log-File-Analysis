

### Maintaining a dictionary of hosts 
def get_hosts_list(inp_row, host_dict):
	host=inp_row[0]
	if host in host_dict:
		host_dict[host]=host_dict[host]+1
	else:
		host_dict[host]=1