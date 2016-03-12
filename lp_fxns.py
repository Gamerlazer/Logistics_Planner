# dest_city = raw_input("What city do you want to plan for? ")
# dest_state = raw_input("What state is this? ")
# dest_state_ab = dictionary

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
