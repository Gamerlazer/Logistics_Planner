# Yelp queries
import rauth
from lp_fxns import *
from states import *

# Google Maps
from cStringIO import StringIO
from PIL import Image
import urllib
import webbrowser # added
new = 2 # added

### Fuction to grab queries
def get_results(params):
	session = rauth.OAuth1Session(
	consumer_key = yelp_api_keys[0],consumer_secret = yelp_api_keys[1],access_token = yelp_api_keys[2],access_token_secret = yelp_api_keys[3])
	request = session.get("http://api.yelp.com/v2/search/",params=params)
	#Transforms the JSON API response into a Python dictionary
	data = request.json()
	return data

# print get_results(yelp_rest_search("houston","tx"))

### Generates a list of user selected restuarants
user_picks = []

def user_choice(dest_city, dest_state_ab,fxn_type,biz_name=None):
	if biz_name != None:
		lib = biz(get_results(fxn_type(biz_name,dest_city,dest_state_ab)))
	else:
		lib = biz(get_results(fxn_type(dest_city,dest_state_ab)))
	user_choice = raw_input("What restaurants did you want to visit? Type the name of the restaurant: \n If you want more reviews, type 'yelp' after the restaurant name: ").lower()
	user_complete = False
	while user_complete != True:
		if user_choice in lib:
			user_picks.append(lib[user_choice])
			user_choice = raw_input("\nWhat other restaurants did you want to visit? \n If you want more reviews, type 'yelp' after the restaurant name. \n When done with this list type exit: ").lower()
		elif user_choice in user_picks:
			user_choice = raw_input("\nOops you already picked that restaurant. Please choose another restaurant. ").lower()
		elif "yelp" in user_choice: #added
			user_choice = user_choice.replace("yelp","").strip() # added
			webbrowser.open(lib[user_choice].url, new=new) # added
		elif user_choice == "exit":
			user_complete = True
		else:
			user_choice = raw_input("\nSorry that wasn't a choice, please try again: ")

### This part works! Get user city and state

dest_city = raw_input("What city do you want to plan for? ") # save the city
dest_state = raw_input("What state is this? ").lower() # save the state

dest_state_ab = ""
valid_state = False
while valid_state != True:
	if dest_state in states: # if user input is a valid state abs then set to dest_state_ab
		dest_state_ab = dest_state
		valid_state = True
	elif dest_state in states_to_ab: # use state dic to convert to abrevation
		dest_state_ab = states_to_ab[dest_state]
		valid_state = True
	else:
		dest_state = raw_input("Please enter a valid state ").lower()

### Searches for city listed above. Gives user options to search between top restaurants, business name or food.
search_complete = False
while search_complete != True:

	search_type = None
	while search_type != "top restaurants" and search_type != "business name" and search_type != "food" and search_type != "map":
		search_type = raw_input("What type of search would you like to complete? \n - Top Restaurants? \n - Business Name? \n - Food? \n - Ready for your map? Type Map \n").lower()
		if search_type == "top restaurants":
			user_choice(dest_city,dest_state_ab,yelp_rest_search)
			search_type = None
		elif search_type == "business name":
			biz_name = raw_input("What is the name of the restaurant you want to search? ")
			user_choice(dest_city,dest_state_ab,yelp_biz_search,biz_name)
			search_type  = None
		elif search_type == "food":
			biz_name = raw_input("What type of food would you like to search? ")
			user_choice(dest_city,dest_state_ab,yelp_biz_search,biz_name)
			search_type  = None
		elif search_type == "map":
			search_complete = True
		else:
			print "Please pick Top Restaurants or Business Name: "

### Generates markers
coordinate_markers = ""
for biz in user_picks:
	coordinate_markers += "&markers=color:red%7Clabel:Longname_here%7C"+str(biz.coordinate[0])+","+str(biz.coordinate[1])

url = "https://maps.googleapis.com/maps/api/staticmap?center="+dest_city+","+dest_state_ab+"&zoom=12&size=1000x800&scale=2&maptype=roadmap"+coordinate_markers+"&key="+google_api_key

buffer = StringIO(urllib.urlopen(url).read())
maps = Image.open(buffer)
maps.show()


