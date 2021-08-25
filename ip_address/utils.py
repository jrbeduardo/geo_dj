from django.contrib.gis.geoip2 import GeoIP2
from google_drive_downloader import GoogleDriveDownloader as gdd
from ipware import get_client_ip

# helper functions
def get_geo(ip):
    g = GeoIP2()
    country = g.country(ip)
    city = g.city(ip)
    lat, lon = g.lat_lon(ip)
    return country, city, lat, lon

def get_center_coodinates(latA, lonA, latB=None, lonB=None):
    cord = (latA, lonA)
    if latB:
        cord =[(latA+latB)/2, (lonA+lonB)/2]
    return cord

def get_zoom(distance):
    if distance <= 150:
        return 10
    elif distance>150 and distance<=1000:
        return 5
    elif distance>1000 and distance<=5000:
        return 3
    else:
        return 2

def get_ip_address(request):
    ip, is_routable = get_client_ip(request)
    if ip is None:
    # Unable to get the client's IP address
        ip='0.0.0.0'
    else:
        # We got the client's IP address
        if is_routable:
            # The client's IP address is publicly routable on the Internet
            ip+=' Public'
        else:
            # The client's IP address is private
            ip+=' Private'
    return ip
