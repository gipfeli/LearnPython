my_name = 'Dat Nguyen'
my_age = 26 # Yep, I'm old
my_height = 170 # cm
my_weight = 75 # kg
my_eyes = 'Brown'
my_teeth = 'Yellow'
my_hair = 'Black'

print "Let's talk about %s." % my_name
print "He's %d cm tall." % my_height
print "He's %d kg heavy." % my_weight
print " Actually he's fat."
print "He's got %s eyes and %s hair" %(my_eyes, my_hair)
print "His teeth are usually %s because of coffee." % my_teeth

# Let do something tricky here
print "If I add %d, %d and %d I get %d." %(my_age, my_height, my_weight, my_age + my_height + my_weight)
print "%(language)s has %(#)05d quote types." % {'language': "Python", '#':2}
print "My name is %(name)s and I'm %(age)d." % {'name': my_name, 'age': my_age}