
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
	params["limit"] = "5" # number of results
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

class Business(object):
	def __init__(self,name,display_address,url, categories,coordinate):
		self.name = name
		self.display_address = display_address
		self.url = url
		self.categories = categories
		self.coordinate = coordinate


def biz(query):
	biz_list_results = {}
	for biz in query["businesses"]:
		print biz["name"]
		street = "" # Clean up address display
		for i in biz["location"]["display_address"]: 
			if i == biz["location"]["display_address"][len(biz["location"]["display_address"])-1]: # don't add line break at end of address
				city= str(i)+"\n"
			elif i == biz["location"]["display_address"][len(biz["location"]["display_address"])-2]:
				neighborhood = str(i)
			else:
				street += str(i)+"\n"
		address = street+city+neighborhood
		print address
		# print biz["url"]
		categories = "" # Clean up category display
		for cats in biz["categories"]:
			if cats[0] == biz["categories"][len(biz["categories"])-1][0]: # don't add comma if last of the list
				categories += cats[0]
			else: 
				categories += cats[0]+", "
		print categories+"\n"
		biz["name"] = str(biz["name"]) #converts unicode to strings
		# biz_list_results.append(biz["name"]) #adds business to list
		
		biz_list_results[biz["name"]] = Business(biz["name"],address,biz["url"],categories,biz["location"]["coordinate"]) #creates a business class for each resturant
	return biz_list_results	

