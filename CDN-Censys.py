import json
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

if __name__ == '__main__':
	akamai = open("Akamai.txt", "w")
    azure = open("Azure.txt", "w")
    baidu = open("Baidu.txt", "w")
	cachefly = open("Cachefly.txt", "w")
	cdnetworks = open("CDNetworks.txt", "w")
	cdnsun = open("CDNsun.txt", "w")
    chinacache = open("ChinaCache.txt", "w")
    cloudflare = open("CloudFlare.txt", "w")
    cloudfront = open("CloudFront.txt", "w")
    edgecast = open("EdgeCast.txt", "w")
    fastly = open("Fastly.txt", "w")
    incapsula = open("Incapsula.txt", "w")
    keycdn = open("KeyCDN.txt", "w")
    leaseweb = open("LeaseWeb.txt", "w")
    limelight = open("Limelight.txt", "w")
    stackpath = open("Stackpath.txt", "w")
    with open("fgxntlcpdw5hsoi9-80-http-get-full_ipv4-20180703T023005-zgrab-results.json", "r") as f:
        for line in f:
            ip_content = json.loads(line)
            try:
                response = ip_content['data']['http']['response']
            except:
                response = 'None'
            ip = ip_content['ip']
            if response == 'None':
                print ip + ' No response.'
            else:
                try:
                    server = response['headers']['server'][0]
                except:
                    server = 'None'
                try:
                    unknown = response['headers']['unknown']
                except:
                    unknown = 'None'
                if 'X-iinfo' in str(unknown):
                    head_icps = 'X-iinfo'
                else:
                    head_icps = 'None'
                try:
                    body = response['body']
                except:
                    body = 'None'
                if server == 'AkamaiGHost':
                    akamai.writelines(ip + '\n')
                    print 'Akamai ' + ip
                elif server == 'ECCAcc':
                    azure.writelines(ip + '\n')
                    print 'Azure ' + ip
                elif server == 'yunjiasu-nginx':
                    baidu.writelines(ip + '\n')
                    print 'Baidu ' + ip
                elif server.startswith('CFS'):
                    cachefly.writelines(ip + '\n')
                    print 'Cachefly ' + ip + ' ' + server
                elif server.startswith('PWS'):
                    cdnetworks.writelines(ip + '\n')
                    print 'CDNetworks ' + ip + ' ' + server
                elif 'worldcdn' in server:
                    cdnsun.writelines(ip + '\n')
                    print 'CDNsun ' + ip + ' ' + server
                elif 'ChinaCache' in server:
                    chinacache.writelines(ip + '\n')
                    print 'ChinaCache ' + ip + ' ' + server
                elif server == 'cloudflare-nginx':
                    cloudflare.writelines(ip + '\n')
                    print 'Cloudflare ' + ip
                elif server == 'CloudFront':
                    cloudfront.writelines(ip + '\n')
                    print 'CloudFront ' + ip
                elif server.startswith('ECS') or server.startswith('ECD') or server.startswith('ECAcc'):
                    edgecast.writelines(ip + '\n')
                    print 'EdgeCast ' + ip + ' ' + server
                elif 'Fastly error' in body:
                    fastly.writelines(ip + '\n')
                    print 'Fastly ' + ip + ' ' + server
                elif ('Incapsula incident ID' in body) or (head_icps != 'None'):
                    incapsula.writelines(ip + '\n')
                    print 'Incapsula ' + ip + ' ' + server
                elif server == 'keycdn-engine':
                    keycdn.writelines(ip + '\n')
                    print 'KeyCDN ' + ip + ' ' + server
                elif 'leasewebcdn' in server:
                    leaseweb.writelines(ip + '\n')
                    print 'LeaseWeb ' + ip + ' ' + server
                elif 'EdgePrism' in server:
                    limelight.writelines(ip + '\n')
                    print 'Limelight ' + ip + ' ' + server
                elif server == 'NetDNA-cache/2.2':
                    stackpath.writelines(ip + '\n')
                    print 'Stackpath ' + ip + ' ' + server
                else:
                    try:
                        print 'Not a CDN node. ' + ip + ' ' + server.encode('utf-8')
                    except Exception as e:
                        print 'Not a CDN node. ' + ip + ' ' + str(e)
    print '--------------Done----------------'
    f.close()
    akamai.close()
    azure.close()
    baidu.close()
    cachefly.close()
    cdnetworks.close()
    cdnsun.close()
    chinacache.close()
    cloudflare.close()
    cloudfront.close()
    edgecast.close()
    fastly.close()
    incapsula.close()
    keycdn.close()
    leaseweb.close()
    limelight.close()
    stackpath.close()