# -*- encoding:utf-8 -*-

the_count = [1,2,3,4,5]
fruits = ['apple', 'orange', 'banana', 'pear', 'grape']
change = [ 1, 'pennies', 2, 'dimes', 3, 'quarters']

for number in the_count:
    print "this is count %d. " %number

for fruit in fruits:
    print "This is a friut of kind %s" %fruit

for i in change:
    print "I got %r" %i

elements = []

for i in range(0,6):
    print "Adding %d to the list" % i
    elements.append(i)

for i in elements:
    print "Elements was: %d" % i






