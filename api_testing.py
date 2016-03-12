
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

def biz(list1):
	for biz in list1["businesses"]:
		biz_name = biz["name"]
		biz_address = biz["location"]["display_address"]
		print biz["url"]
		print biz["categories"]	
		print biz["location"]["coordinate"]
		

		

print biz(get_results(yelp_rest_search("san francisco","ca")))
# print get_results(yelp_rest_search("san francisco","ca"))["businesses"][0]["name"]
# print get_results(yelp_rest_search("san francisco","ca"))["businesses"][0]["url"]
# print get_results(yelp_rest_search("san francisco","ca"))["businesses"][0]["categories"]
# print get_results(yelp_rest_search("san francisco","ca"))["businesses"][0]["location"]["display_address"]
# print get_results(yelp_rest_search("san francisco","ca"))["businesses"][0]["location"]["coordinate"]