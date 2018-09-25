import socket
import ssl
import urllib2
import json

def get_response(proto,ip,host,url):
	try:
		Header = "GET "+url+"  HTTP/1.1\nHost: "+host+"\nConnection: keep-alive\nAccept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8\nUser-Agent: Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36\nAccept-Language: zh-CN,zh;q=0.8\n\n"
		if proto == "http":
			socket.setdefaulttimeout(4)
			s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
			s.connect((ip,80))
			s.send(Header)
			buff = s.recv(1024)
			print "http " + host + " " + ip
			print buff
			# lease_resp.writelines(buff + '\n')
		else:
			socket.setdefaulttimeout(4)
			s = ssl.wrap_socket(socket.socket())
			s.connect((ip,443))
			s.send(Header)
			buff = s.recv(1024)
			print "https " + host + " " + ip
			print buff
	except Exception,e:
	 	print e

def ip_area(ip):
	try:
		apiurl = "http://ip-api.com/json/%s" % ip
		content = urllib2.urlopen(apiurl).read()
		data = json.loads(content)
		if data['status'] == 'success':
			print "Country: " + data['country'] 
			print "Region: " + data['regionName']
			print "City: "  + data['city']
			print "ISP: " + data['isp']
			# lease_resp.writelines(data['country'] + " " + data['city'] + " " + data['regionName'] + " " + data['isp'] + '\n')
		else:
			print 'None'
			# lease_resp.writelines('None' + '\n')
	except Exception,e:
		print e

if __name__ == "__main__":
	# stack_ip = open("Stackpath_ipblock.txt", "r")
	# stack_resp = open("Leaseweb_resp.txt", "w")
	# for ip in stack_ip.readlines():
	ip = '54.203.41.46'
		# lease_resp.writelines(ip + '\n')
	get_response("http", ip, "www.malaysiaairlines.com", "/")
	ip_area(ip)
	# lease_ip.close()
	# www.malaysiaairlines.com

