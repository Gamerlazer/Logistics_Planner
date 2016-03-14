# while not exit

# ask user to add to the list

# if user types exit, they're done with the adding to selections.

class Family(object):
	def __init__(self,name,age):
		self.name = name
		self.age = age

family = [["Julie",4],["Tony",3],["Binh",2]]

def creating_family(list1):
	family1 = {}
	for person in list1:
		family1[person[0]] = Family(person[0],person[1])
	return family1

dictionary = creating_family(family)

print dictionary

user_picks = {}

user_input = raw_input("Where did you want to go? ")

while user_input != "exit":
	if user_input in dictionary
		user_picks[user_picks] =
		user_input = raw_input("Where else did you want to go? ")
print user_picks