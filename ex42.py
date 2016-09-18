## Animal is-an Obj
class Animal(object):
	pass

## Dog is an Animal
class Dog(Animal):
	def __init__(self, name):
		self.name = name

## Cat is an Animal
class Cat(Animal):
		def __init__(self, name):
			self.name = name

## Person is-an Obj
class Person(object):
	def __init__(self, name):
		self.name = name
		self.pet = None

## Employee is a Person
class Employee(Person):
	def __init__(self, name, salary):
		## Some of strange magic: super(Employee, self) == self
		## Otherwise, we have to write it like this: Person.__init__(self)
		super(Employee, self).__init__(name)
		self.salary = salary

## Fish is an Obj
class Fish(object):
	pass

## Salmon is a Fish
class Salmon(Fish):
	pass

## Halibut is a Fish
class Halibut(Fish):
	pass

## Rover is a Dog
rover = Dog("Rover")

## Satan is a Cat
satan = Cat("Satan")

## Mary is a Person
mary = Person("Mary")

## Mary's pet is Satan
mary.pet = satan

## Frank is an Employee, with a salary of 120000
frank = Employee("Frank", 120000)

## Frank's pet is Rover
frank.pet = rover

## Flipper is a Fish
flipper = Fish()

## Crouse is a Salmon
crouse = Salmon()

## Harry is a Halibut
harry = Halibut()


