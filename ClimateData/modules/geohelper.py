from geopy import geocoders

gn = geocoders.GeoNames(username="worldclimate")
def get_lat_long(location):
    concat_location = location['city_name'] + ", " + location['country']
    geoinfo = gn.geocode(concat_location)
    print(geoinfo)
    return geoinfo.latitude, geoinfo.longitude

