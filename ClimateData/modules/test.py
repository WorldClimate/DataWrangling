from geopy import geocoders

gn = geocoders.GeoNames(username="worldclimate")
geoinfo = gn.geocode('San Francisco, California, United States')
print(geoinfo)
