user_name = "Tosin"
password = "Difficult"

user_name1 = input("Please enter your username: " )
password1 = input("Please enter your password: " )

if(user_name != user_name1 and password == password1):
    print("Invalid username")
elif(user_name == user_name1 and password != password1):
    print("Invalid password")
elif(user_name != user_name1 and password != password1):
	print("Invalid username and password")
else:
	print("You are now logged in")
