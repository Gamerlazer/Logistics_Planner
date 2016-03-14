# Yelp queries
import rauth
from lp_fxns import *
from states import *

# Google Maps
from cStringIO import StringIO
from PIL import Image
import urllib

# Fuction to grab queries
def get_results(params):
	session = rauth.OAuth1Session(
	consumer_key = yelp_api_keys[0],consumer_secret = yelp_api_keys[1],access_token = yelp_api_keys[2],access_token_secret = yelp_api_keys[3])
	request = session.get("http://api.yelp.com/v2/search/",params=params)
	#Transforms the JSON API response into a Python dictionary
	data = request.json()
	return data

### This part works! Get user city and state

dest_city = raw_input("What city do you want to plan for? ") # save the city
dest_state = raw_input("What state is this? ").lower() # save the state

# set dest_state_ab to the lowercase abrevation of state
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

biz(get_results(yelp_rest_search(dest_city,dest_state_ab)))
lib  = biz(get_results(yelp_rest_search(dest_city,dest_state_ab))) #creates a storage for results



### Generates a list of user selected restuarants

user_picks = []
user_choice = raw_input("What restaurants did you want to visit? Type name of restaurant: ")
user_complete = False
while user_complete != True:
	if user_choice in lib:
		user_picks.append(lib[user_choice].name)
		user_choice = raw_input("What other restaurants did you want to visit? When ready for your map, type exit when done with your choices: ")
	elif user_choice in user_picks:
		user_choice = raw_input("Oops you already picked that restaurant. Please choose another restaurant. When ready for your map, type exit when done with your choices: ")
	elif user_choice == "exit":
		user_complete = True
	else:
		user_choice = raw_input("Sorry that wasn't a choice, please try again: ")


# lib  = biz(get_results(yelp_rest_search("oakland","ca"))) #testing 
# user_picks = ["Ba-Bite","Smelly's Creole & Soul Food"] #testing

# Generates markers
coordinate_markers = ""
for rest in user_picks:
	coordinate_markers += "&markers=color:red%7Clabel:A%7C"+str(lib[rest].coordinate[0])+","+str(lib[rest].coordinate[1])

url = "https://maps.googleapis.com/maps/api/staticmap?center="+dest_city+","+dest_state_ab+"&zoom=12&size=600x300&maptype=roadmap"+coordinate_markers+"&key="+google_api_key

buffer = StringIO(urllib.urlopen(url).read())
maps = Image.open(buffer)
maps.show()



# for c in range(len(user_picks)): # Shows a list to the user of the restaurants they chose
# 	print user_picks[c].name
