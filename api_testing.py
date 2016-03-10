
import rauth

# Open file with API Keys
with open("api_key.txt") as yelp_api:
	yelp_keys = yelp_api.readlines()

# Clean up API Keys
yelp_api_keys = []
for k in yelp_keys:
	yelp_api_keys.append(k.split(':')[1].replace('\n',''))
# Save google API Key
google_api_key = yelp_api_keys[4]


# Fuction to grab queries
def get_results(params):
	session = rauth.OAuth1Session(
	consumer_key = yelp_api_keys[0],consumer_secret = yelp_api_keys[1],access_token = yelp_api_keys[2],access_token_secret = yelp_api_keys[3])
	request = session.get("http://api.yelp.com/v2/search",params=params)
	#Transforms the JSON API response into a Python dictionary
	data = request.json()
	return data

# # Ask user for city 


# Fuction to generate query parameters
def yelp_rest_search(x):
	pass

# Fuction to generate activity query parameters
def yelp_activities_search(x):
	pass



