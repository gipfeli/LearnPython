# This one is similiar to using argument argv
def print_two(*args):
	arg1, arg2 = args
	print "arg1: %r, arg2: %r" % (arg1,arg2)

# Without pointer
def print_two_again(arg1, arg2):
	print "arg1: %r, arg2: %r" % (arg1, arg2)

# Take one argument
def print_one(arg1):
	print "arg1: %r" % (arg1)

# Take none argument
def print_none():
	print "I got nothing."

print_two("Dat", "Nguyen")
print_two_again("Dat", "Nguyen")
print_one("Dat")
print_none()