#This is the program to test understanding of use of json
import json

try:
	with open('username.json', 'r') as userfile_object:
		username=json.load(userfile_object)
except FileNotFoundError:
	username=input("Enter your username ")
	with open('username.json', 'w') as userfile_object:
		json.dump(username, userfile_object)
		print('Hello ' + username + '. We will remember you when you come back!!')

else:
	print('Welcome back ' + username.title())

