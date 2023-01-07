import googlemaps
import gmplot
from config import GOOGLE_MAPS_GEOCODING_API_KEY

gmaps = googlemaps.Client(key=GOOGLE_MAPS_GEOCODING_API_KEY)

def get_geolocation(address):
    geocode_result = gmaps.geocode(address)

    latitude = geocode_result[0]['geometry']['location']['lat']
    longitude = geocode_result[0]['geometry']['location']['lng']
    return {'lat': latitude, 'long': longitude}

def plot_map(map_center, geolocations, map_title):
    gmap = gmplot.GoogleMapPlotter(map_center['lat'], map_center['long'], 16)

    for geolocation in geolocations:
        gmap.marker(geolocation['lat'], geolocation['long'])
    gmap.draw(map_title + '.html')