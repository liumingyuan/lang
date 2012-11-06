# -*- encoding:utf-8 -*-

# this document is about reading file

from sys import argv

script, filename = argv

txt = open(filename)

print "Here's your file %r:" % filename
print txt.read()

print "Type the fileName again:"
filename = raw_input('> ')

txt = open(filename)
print txt.read()