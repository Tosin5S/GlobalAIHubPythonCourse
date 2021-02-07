#The keys are the usernames
#Values are passwords

login_data = {"Tosin":"lekan","Bolu":"badju", "Kolade" : "pretty"}

username = input("Please enter your username: " )
password = input("Please enter your password: " )
	     
if(username not in login_data.keys()):
    print("Invalid username")
elif(username in login_data.keys() and password != login_data[username]):
    print("Invalid password")
elif(username in login_data.keys() and password == login_data[username]):
	print("You are now logged in")
#just in case of any bugs
else:
	print("Try again !")
