# dest_city = raw_input("What city do you want to plan for? ")
# dest_state = raw_input("What state is this? ")
# dest_state_ab = dictionary

# Open file with API Keys
with open("api_key.txt") as yelp_api:
	yelp_keys = yelp_api.readlines()

# Convert keys to a list
yelp_api_keys = []
for k in yelp_keys:
	yelp_api_keys.append(k.split(':')[1].replace('\n',''))

# Save google API Key
google_api_key = yelp_api_keys[4]

# Restaurant searches 
def yelp_rest_search(dest_city,dest_state_ab):
	params = {}
	params["term"] = "restaurants"
	params["location"] = dest_city+", "+dest_state_ab
	params["sort"] = "2"
	params["limit"] = "10"
	params["category_filter"] = "restaurants"
	return params
	

# Restaurant name search
def yelp_biz_search(biz_name,dest_city,dest_state_ab):
	params = {}
	params["term"] = biz_name
	params["location"] = dest_city+", "+dest_state_ab
	params["sort"] = "0"
	params["limit"] = "10"
	params["category_filter"] = "restaurants"
	return params

# Fuction to generate activity query parameters
def yelp_activities_search(x):
	pass
