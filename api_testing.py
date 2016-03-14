
import rauth
from lp_fxns import *
from states import *

# Fuction to grab queries
def get_results(params):
	session = rauth.OAuth1Session(
	consumer_key = yelp_api_keys[0],consumer_secret = yelp_api_keys[1],access_token = yelp_api_keys[2],access_token_secret = yelp_api_keys[3])
	request = session.get("http://api.yelp.com/v2/search/",params=params)
	#Transforms the JSON API response into a Python dictionary
	data = request.json()
	return data
### This part works! Get user city and state

# dest_city = raw_input("What city do you want to plan for? ") # save the city
# dest_state = raw_input("What state is this? ").lower() # save the state

# # make sure user entry is a real state
# valid_state = False

# while valid_state != True:
# 	if dest_state in states:
# 		dest_state_ab = dest_state
# 		valid_state = True
# 	elif dest_state in states_to_ab:
# 		dest_state_ab = states_to_ab[dest_state]
# 		valid_state = True
# 	else:
# 		dest_state = raw_input("Please enter a valid state ").lower()


# print biz(get_results(yelp_rest_search("san francisco","ca")))

# lib  = biz(get_results(yelp_rest_search(dest_city,"ca"))) #creates a storage for results


# user_picks = []
# user_picks.append(lib['Birba'])
# print user_picks[0].coordinate

# if lib['Birba'] in user_picks:
# 	print "in list"
# else:
	# "not in list"

# What places did you want to go to?
# While loop, not exit/done keep asking



# user_input = raw_input("Where did you want to go? ")

# while user_input != "exit":
# 	if user_input in library:
# 		user_picks.append(user_input)
# 		user_input = raw_input("Where else did you want to go? ")
# 	else:
# 		user_input = raw_input("Please choose from list above: ")
# print user_picks




# print get_results(yelp_rest_search("san francisco","ca"))["businesses"][0]["name"]
# print get_results(yelp_rest_search("san francisco","ca"))["businesses"][0]["url"]
# print get_results(yelp_rest_search("san francisco","ca"))["businesses"][0]["categories"]
# print get_results(yelp_rest_search("san francisco","ca"))["businesses"][0]["location"]["display_address"]
# print get_results(yelp_rest_search("san francisco","ca"))["businesses"][0]["location"]["coordinate"]

