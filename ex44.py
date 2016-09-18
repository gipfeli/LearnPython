class Parent(object):
	def override(self):
		print "PARENT override()"

	def implicit(self):
		print "PARENT implicit()"

	def altered(self):
		print "PARENT altered()"

class Child(Parent):
	def override(self):
		print "CHILD override()"

	def altered(self):
		print "CHILD, BEFORE PARENT altered()"
		super(Child, self).altered() ## Use 'super' for multiple inheritance, which is when, you define a class that inherits from one or more classes.
		print "CHILD, AFTER PARENT altered()"

dad = Parent()
son = Child()

dad.implicit()
son.implicit() ## Child-Class inherited the same-named function in Parent-Class

dad.override()
son.override()

dad.altered()
son.altered()