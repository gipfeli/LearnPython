class Parent(object):

	def implicit(self):
		print "PARENT implicit()"

class Child(Parent): ## An empty class - Child, inherit all defined functions in Parent
	pass

dad = Parent()
son = Child()

dad.implicit()
son.implicit()
		