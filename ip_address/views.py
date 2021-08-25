import folium
import geoip2.database
from geopy.geocoders import Nominatim
from geopy.distance import geodesic
from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView
from .models import Visitor, Measurement
from .forms import MeasurementModelForm
from .utils import get_geo, get_center_coodinates, get_zoom, get_ip_address
# Create your views here.


def calculate_distance_view(request):
    #initial Values
    distance = None
    destination = None
    total_visitors = Visitor.objects.all().count()
    form = MeasurementModelForm(request.POST or None)
    geolocator = Nominatim(user_agent='ip_address')
    ip, ip_status = get_ip_address(request)
    country, city, l_lat, l_lon = get_geo(ip)
    location = geolocator.geocode(city)

    # location coordinates
    pointA = (l_lat, l_lon )


    # Initial folium map
    m = folium.Map(width=800, height=500,
        location=get_center_coodinates(l_lat, l_lon),
        zoom_start=1)


    # draw visitors
    for visitor in Visitor.objects.all():
        folium.Marker([visitor.latitud, visitor.longitud], tooltip='click here for more',
            popup='hi', icon=folium.Icon(color='purple', icon='user')).add_to(m)

    # new visitor
    folium.Marker([l_lat, l_lon], tooltip='click here for more',
        popup='you', icon=folium.Icon(color='red', icon='user')).add_to(m)

    # register visitor
    if Visitor.objects.filter(ip=ip, latitud = l_lat, longitud= l_lon).count()==0:
        visitor = Visitor.objects.create(
            ip = ip,
            latitud = l_lat,
            longitud= l_lon
        )
    if form.is_valid():
        instance = form.save(commit=False)
        destination_ = form.cleaned_data.get('destination')
        destination = geolocator.geocode(destination_)
        d_lat = destination.latitude
        d_lon = destination.longitude

        # destination coordinates
        pointB = (d_lat, d_lon)

        # distance calculation
        distance= round(geodesic(pointA, pointB).km,2)

        # folium map modification
        m = folium.Map(width=800, height=500,
            location= get_center_coodinates(l_lat, l_lon, d_lat, d_lon),
            zoom_start=get_zoom(distance)
        )
        # location Marker
        folium.Marker([l_lat, l_lon], tooltip='click here for more',
            popup=city['city'], icon=folium.Icon(color='red', icon='user')).add_to(m)
        # destination Marker
        folium.Marker([d_lat, d_lon], tooltip='click here for more',
            popup=destination, icon=folium.Icon(color='purple', icon='heart')).add_to(m)
        # draw line
        line = folium.PolyLine(locations=[pointA, pointB], weight=5, color='red')
        m.add_child(line)

        instance.location = location
        instance.distance= distance
        instance.save()

    m = m._repr_html_()
    context ={
        'distance': distance,
        'form': form,
        'map': m,
        'destination': destination,
        'ip': ip,
        'ip_status': ip_status,
        'total_visitors': total_visitors
    }
    return render(request, 'base/main.html', context)
