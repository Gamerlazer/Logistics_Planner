
import rauth

# obtain yelp api keys
with open(".gitignore") as yelp_api:
	yelp_keys = yelp_api.readlines()

yelp_api_keys = []
for k in yelp_keys:
	yelp_api_keys.append(k.split(':')[1].replace('\n',''))

consumer_key = yelp_api_keys[0]
consumer_secret = yelp_api_keys[1]
token = yelp_api_keys[2]
token_secret = yelp_api_keys[3]

print yelp_api_keys

def get_results(params):

	session = rauth.OAuth1Session(
	consumer_key = consumer_key
	,consumer_secret = consumer_secret
	,access_token = token
	,access_token_secret = token_secret)
	 
	request = session.get("http://api.yelp.com/v2/search",params=params)

	#Transforms the JSON API response into a Python dictionary
	data = request.json()
	

	return data


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