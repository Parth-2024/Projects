import geocoder
from geopy.geocoders import Nominatim
#Current Location in form of longitude
def get_location():
	''' Get your IP-based location'''
	g = geocoder.ip('me')
	latlng = g.latlng
				
	if not latlng:
		raise Exception("Could not get the location. Make sure you're connected to the internet.")

	latitude, longitude = latlng

	# Use geopy to get the location name
	geolocator = Nominatim(user_agent="geoapiExercises")
	location = geolocator.reverse((latitude, longitude), exactly_one=True)

	location_name = location.address if location else "Location name not found"

	return latitude, longitude, location_name
latitude, longitude, location_name=get_location()
print(latitude, longitude, location_name)