import urllib.request
import requests
import dns.resolver
import json


def get_addrinfo(nameservers, qname): # nameservers is dns, qname is the hostname which you want to resolve
    tmp = dns.resolver.Resolver()
    tmp.nameservers = nameservers # A list of nameservers to query
    tmp.lifetime = 3.0 # The total number of seconds to spend trying to get an answer to the question.(float)
    ans = tmp.query(qname) # Query nameservers to find the answer to the question, Returns: dns.resolver.Answer instance
    result = [a.address for a in ans.rrset.items] # rrset: The answer
    return result

def url_ip(url):
	if url.startswith("http://"):
		host = url[7:] # get rid of http://
	elif url.startswith("https://"):
		host = url[8:] # get rid of https://
	else:
		host = 'None'
		print("url error!")

	if host != 'None':
		print("Host: ", host)
		# iplist.writelines(url + "\n")

		DNS = open("truedns", "r")
		ip_list = []
		ip_num = 0
		for d in DNS.readlines():
			try:
				IP = get_addrinfo([d.strip("\n")], host)
				for ip in IP:
					if ip not in ip_list:
						ip_list.append(ip)
						# iplist.writelines(ip + "\n")
						ip_num += 1
						print("IP Address: ", ip)
						ip_area(ip)
			except:
				print("None")
		try:
			r = requests.get(url)
		except:
			print("url get error!")
		try:
			status = r.status_code
			print("Status_code: ", status)
		except:
			status = "None"
			print("Status KeyError")
		try:
			server = r.headers["server"]
			print("Server: ", server)
		except:
			server = "None"
			print("Server KeyError")
		# iplist.writelines(str(status) + " " + server + "\n")
		print("----DNS Resolve Complete!----")


def ip_area(ip):
	try:
		apiurl = "http://ip-api.com/json/%s" % ip
		content = urllib.request.urlopen(apiurl).read()
		data = json.loads(content)
		if data['status'] == 'success':
			print("Country: ", data['country'])
			print("Region: ", data['regionName'])
			print("City: ", data['city'])
			print("ISP: ", data['isp'])
			# ip_dict[ip] = {'country' : data['country'], 'region' : data['regionName'], 'city' : data['city'], 'isp' : data['isp']}
			# iplist.writelines(data['country'] + " " + data['city'] + " " + data['regionName'] + " " + data['isp'] + "\n")
		else:
			print('None')
	except Exception as e:
		print(e)
 
if __name__ == '__main__':
	url = input("Please enter url: ")
	# iplist = open("cdn_iplist.txt","w")
	# ip_dict = {}
	url_ip(url)
	# with open("cdn_iplist.json", "w") as f:
	# 	json.dump(ip_dict, f, ensure_ascii = False, encoding = 'utf-8', indent = 4, separators = (',', ': '))
	# iplist.close()
