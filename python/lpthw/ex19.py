# -*- encoding:utf-8 -*-

# Functions and variables Demo Program

def cheese_and_crackers( cheese_count, boxes_of_crackers):
    print "you've %d cheese!" %cheese_count
    print "you've %d boxes of crakers"%boxes_of_crackers
    print "Man that's not enough for a party!"
    print "Get a blanket.\m"


print "we can just give the function numbers directly:"
cheese_and_crackers(20,30)

print "Or, we can use variables from our script:"
amount_of_cheese = 10
amount_of_crackers = 50
cheese_and_crackers( amount_of_cheese, amount_of_crackers)

print "Or do some calculation in the parathesis:"
cheese_and_crackers( 20+5, 20+6);

print "Or:"
cheese_and_crackers( amount_of_cheese + 100, amount_of_crackers + 1000)


