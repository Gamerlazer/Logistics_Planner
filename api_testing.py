
import rauth
from lp_fxns import *
from states import states

# Fuction to grab queries
def get_results(params):
	session = rauth.OAuth1Session(
	consumer_key = yelp_api_keys[0],consumer_secret = yelp_api_keys[1],access_token = yelp_api_keys[2],access_token_secret = yelp_api_keys[3])
	request = session.get("http://api.yelp.com/v2/search/",params=params)
	#Transforms the JSON API response into a Python dictionary
	data = request.json()
	return data

class Business(object):
	def __init__(self,name,display_address,url, categories,coordinate):
		self.name = name
		self.display_address = display_address
		self.url = url
		self.categories = categories
		self.coordinate = coordinate


def biz(query):
	biz_list_results = []
	for biz in query["businesses"]:
		print biz["name"]
		# print biz["location"]["display_address"]
		# print biz["url"]
		categories = ""
		for cats in biz["categories"]:
			if cats[0] == biz["categories"][len(biz["categories"])-1][0]: # don't add comma if last of the list
				categories += cats[0]
			else: 
				categories += cats[0]+", "

		print categories
		# print biz["categories"]
		biz["name"] = str(biz["name"]) #converts unicode to strings
		biz_list_results.append(biz["name"]) #adds business to list
		biz["name"] = Business(biz["name"],biz["location"]["display_address"],biz["url"],biz["categories"],biz["location"]["coordinate"]) #creates a business class for each resturant
		 

# biz["name"] = Business
# biz_address = biz["location"]["display_address"]
# biz_url = biz["url"]
# biz_categories = biz["categories"]	
# biz_coordinates = biz["location"]["coordinate"]


# def biz(list1):
# 	biz_results = []
# 	for biz in list1["businesses"]:
# 		biz_results["name"] = biz["name"]
# 		biz_address = biz["location"]["display_address"]
# 		biz_url = biz["url"]
# 		biz_categories = biz["categories"]	
# 		biz_coordinates = biz["location"]["coordinate"]
# 	print biz_results

print biz(get_results(yelp_rest_search("san francisco","ca")))
# print get_results(yelp_rest_search("san francisco","ca"))["businesses"][0]["name"]
# print get_results(yelp_rest_search("san francisco","ca"))["businesses"][0]["url"]
# print get_results(yelp_rest_search("san francisco","ca"))["businesses"][0]["categories"]
# print get_results(yelp_rest_search("san francisco","ca"))["businesses"][0]["location"]["display_address"]
# print get_results(yelp_rest_search("san francisco","ca"))["businesses"][0]["location"]["coordinate"]