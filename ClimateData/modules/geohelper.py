from geopy import geocoders

gn = geocoders.GeoNames(username="worldclimate")
def get_lat_long(location):
    geoinfo = gn.geocode(location)
    return geoinfo.latitude, geoinfo.longitude

