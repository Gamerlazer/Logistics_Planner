
def get_search_parameters(lat,long):
	#See the Yelp API for more details
	params = {}
	params["term"] = "restaurant"
	params["ll"] = "{},{}".format(str(lat),str(long))
	params["radius_filter"] = "2000"
	params["limit"] = "10"

	return params	
# print get_search_parameters(37.7833,-122.4167)
print get_results(get_search_parameters(37.7833,-122.4167))



## Google API for custom markers

Request
center: Australia
size: 640x400
style: element:labels|visibility:off
style: element:geometry.stroke|visibility:off
style: feature:landscape|element:geometry|saturation:-100
style: feature:water|saturation:-100|invert_lightness:true
key: API_KEY

## 
http://maps.googleapis.com/maps/api/staticmap?center=Australia&size=640x400&style=element:labels|visibility:off&style=element:geometry.stroke|visibility:off&style=feature:landscape|element:geometry|saturation:-100&style=feature:water|saturation:-100|invert_lightness:true&key=YOUR_API_KEY

AIzaSyCuwSzU40msMCb4KMN70WPnEc9sNwsikzs