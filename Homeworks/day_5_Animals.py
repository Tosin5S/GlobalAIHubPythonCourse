class Animals:
	
	def __init__ (self, name = " ", colour = " ", type = " ", age = 0):
		self.name = name
		self.colour = colour
		self.type = type
		self.age = age
		
	def setName(self,name):
		self.name = name
		
	def getName(self):
		return self.name
		
	def setColour(self,colour):
		self.colour = colour
		
	def setType(self,type):
		self.type = type
		
	def setAge(self,age):
		self.age = age
		
	def getAge(self):
		return "{0} years".format(self.age)
		
	def __str__(self):
		return "{0} is a {1} {2} aged {3} years." .format(self.name, self.colour, self.type, self.age)
		
class Dogs(Animals):
	def __init__ (self, name = " ", colour = " ", age = 0):
		self.name = name
		self.colour = colour
		self.type = "Dog"
		self.age = age
		
	def setType(self, type):
		print("{0} refuses to change type, it will always be a {1} in this Life." .format(self.name, self.type))
		
	def setAge(self, age):
		self.age = age
		
dog = Dogs("Lucky", "black", 6)
print(dog)

dog.setAge(10)
dog.getAge()

dog.setType("Cat")
dog.setName("Smart")
print(dog)

class Cats(Animals):
	def setAge(self,age):
		self.age = age
		
	def getAge(self):
		return"{0} years old." .format(self.age)
		
	def __str__(self):
		return("{0} is {1} years old {2} cat." .format(self.name, self.age, self.colour))
		
	def say(self):
		print("{0} says Meow, Meow, Meow!".format(self.name))
		
cat = Cats("Tussy","yellow",4)
print(cat)

cat.setAge(8)
print(cat.getAge())
print(cat)
cat.say()
	
	
		
	
	