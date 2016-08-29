from sys import argv

script, filename = argv

print "We're going to erase %r." % filename
print "If you don't want that, press CTRL+C."
print "If you want that, press ENTER."

raw_input("?")

print "Opening the file ..."
target = open(filename, 'w')

# Truncating is not needed after open the file. This part means, we open the file, 
# creating it if it doesn't exist and truncating it to 0 bytes if it does. 
# Then, on the next line, we truncate it to 0 bytes.
print "Truncating the file ..."
target.truncate() 

print "Now I'm going to ask you for 3 lines."

line1 = raw_input("Line 1: ")
line2 = raw_input("Line 2: ")
line3 = raw_input("Line 3: ")

print "I'm going to write this to file..."

#target.write(line1)
#target.write("\n")
# target.write(line2)
# target.write("\n")
# target.write(line3)
# target.write("\n")

target.write(line1,"\n",line2,"\n",line3,"\n")

print "And finally, we close it."
target.close()