def add(a, b):
	print "ADDING %d + %d" % (a, b)
	return a + b

def subtract(a, b):
	print "SUBTRACTING %d - %d" % (a, b)
	return a - b

def multiply(a, b):
	print "MULTIFLYING %d * %d" % (a ,b)
	return a * b

def divide(a, b):
	print "DIVIDING %d / %d" % (a, b)
	return a / b

print "Let's do some math with just functions:"

age = add(30, 5)
height = subtract(170, -5)
weight = multiply(50, 5)
iq = divide(100, 2)
print "Age: %d, Height: %d, Weight: %d, IQ: %d" % (age, height, weight, iq)

# Magic
what = add(age, subtract(height, multiply(weight, divide(iq,2))))

print "Magic: ", what