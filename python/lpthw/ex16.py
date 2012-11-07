# -*- encoding:utf-8 -*-

# close
# read
# readline
# truncate
# write(stuff)

from sys import argv
script, filename = argv

print "We're going to erase %r." % filename
print "If you don't want that, hit CTRL-C"
print "If you want to do that hit RETURN"

raw_input("?")

print "Opening the file ..."
target = open(filename, "w")

print "Truncating the file, bye"
target.truncate()

print 'Put three lines into the file'
line1 = raw_input("First line:")
line2 = raw_input("Second line:")
line3 = raw_input("Third line:")

print "I'm going to write those to the file"

target.write(line1 + "\n")
target.write(line2 + "\n")
target.write(line3 + "\n")

print "Finally, we close it"
target.close()