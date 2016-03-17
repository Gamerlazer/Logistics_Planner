# from lp_fxns import *
# # while not exit

# # ask user to add to the list

# # if user types exit, they're done with the adding to selections.

# #search type

# # fxn yelp_rest_search
# # fxn yelp_biz_search
# # parameters shoots back 


# search_complete = False
# while search_complete != True:
# 	search_type = raw_input("What type of search would you like to complete? \n - Top Restaurants \n - Business Name: ").lower()
# 		if search_type == "top restaurants":
# 			lib = biz(get_results(yelp_rest_search(dest_city,dest_state_ab)))
# 		elif search_type == "business name":
# 			biz_name = raw_input("What business would you like to add? ")
# 			yelp_biz_search()

import webbrowser
new = 2
url= "https://www.yelp.com/biz/alamar-oakland-2"
webbrowser.open(url, new=new)