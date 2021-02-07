class Employees:

#You have to enter emloyees's key as username first and 
#manager's key as username the second time. e.g Kolade442.	
	
	employees = {
   "Kolade442" : {
    "first_name" : "Kolade",
    "last_name" : "Kamil",
    "age" : 22,
    "languages" : {"English","Arabic","French"}
  },
 "Bolu553" : {
    "first_name" : "Boluwatife",
    "last_name" : "Caleb",
    "age" : 21,
    "languages" : {"English","Chinese","Hindi"}
  },
  "Tosin555" : {
    "first_name" : "Qudus",
    "last_name" : "Aileru",
    "age" : 21,
   "languages" : {"English","Arabic","French","Hindi"}
  }
}
			
	def __init__(self,username):
		  self.username = input("please enter an employee's username: ")
		  print("checking whether \"{}\" is an employee ... ".format(self.username))
		  
	def getData(self,employeeData):
		  self.employeeData = employeeData
		  		  	
	def showInfo(self):
		  if (self.username in self.employeeData.keys()):
		      first_name = self.employeeData[self.username]["first_name"]
		      last_name = self.employeeData[self.username]["last_name"]	      
		      languages = self.employeeData[self.username]["languages"]
		      print(first_name,last_name, end = " speaks ")
		      for lang in languages:
		  	    print(lang, end = " , ")
		      print("\n")
		  else:
		  	print("Invalid username, please enter the right username")
			      		  		  		  		  
employee = Employees("")
employeeData = employee.employees
employee.getData(employeeData)
employee.showInfo()
			    
class Managers(Employees):
	
	managers = {
   "Esther111" : {
    "first_name" : "Esther",
    "last_name" : "Osunkeye",
    "age" : 28,
    "languages" : {"English","Arabic","French"}
  },
 "Yussuf212" : {
    "first_name" : "Yussuf",
    "last_name" : "Abidemi",
    "age" : 26,
    "languages" : {"English","Chinese","Hindi"}
  },
  "Hassan444" : {
    "first_name" : "Hassan",
    "last_name" : "Lameed",
    "age" : 25,
   "languages" : {"English","Arabic","French","Hindi"}
  }
}	

	def __init__(self,username):
		#a manager is different from an employee so I am not usingsuper().__init__(username)
		self.username = input("please enter a manager's username: ")
		print("checking whether \"{}\" is a manager ... " .format(self.username))
			
manager = Managers("")
employeeData = manager.managers
manager.getData(employeeData)
manager.showInfo()
		



		
		  
		  
	