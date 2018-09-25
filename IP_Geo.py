# import pygeoip, signal, os, sys, threading
import geoip2.database
import json

# Geoipv2
def geoip_query(ip_address):
    #reader_city = geoip2.database.Reader('./GeoLite2-City/GeoLite2-City.mmdb')
    reader_city = geoip2.database.Reader('./GeoLite2-City.mmdb')
	
    try:
        response_city = reader_city.city(ip_address)
        country_code = response_city.country.iso_code
        city = response_city.city.name
        lat = response_city.location.latitude
        lon = response_city.location.longitude

        if country_code == None:
            country_code = ""
        if city == None:
            city = ""
        if lat == None:
            lat = ""
        else:
            lat = str(lat)
        if lon == None:
            lon = ""
        else:
            lon = str(lon)

    except geoip2.errors.AddressNotFoundError:
        country_code = city = lat = lon = ""

    return [country_code, city.replace("\\", " ").replace("\"", " "), lat, lon]

if __name__ == "__main__":
	f_ip = open("./data/Cachefly.txt", "r")
	f_geo = open("./Geo/Cachefly.txt", "w")
	ip_dict = {}
	for ip in f_ip.readlines():
		ip_address = ip.strip("\n")
		geo = geoip_query(ip_address)
		print(ip_address + str(geo))
		ip_dict[ip_address] = {'country_code' : geo[0], 'city' : geo[1], 'lat' : geo[2], 'lon' : geo[3]}
		f_geo.writelines(ip_address + " " + geo[0] + " " + geo[1] + " " + geo[2] + " " + geo[3] + "\n")
	with open("./Geo/Cachefly.json", "w") as f:
		json.dump(ip_dict, f, ensure_ascii = False, indent = 4, separators = (',', ': '))
	f_ip.close()
	f_geo.close()







