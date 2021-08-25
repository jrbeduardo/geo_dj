from django.contrib.gis.geoip2 import GeoIP2
from google_drive_downloader import GoogleDriveDownloader as gdd


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
    x_forwarded_for = request.META.get('HTTP_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[-1].strip()
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip
