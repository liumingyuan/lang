# -*- encoding:utf-8 -*-

from sys import argv

script, username = argv

prompt = '> '

print 'Hi %s, I\' the %s script.' %(username, script)
print 'i\'d like to ask a few questions.'
print "Do you like me?"
likes = raw_input(prompt)

print 'where do you live?'
lives = raw_input(prompt)

print 'what kind of computer do you have?'
computer = raw_input(prompt)

print """
Alright, so you said %r about liking me.
You live in %r.  Not sure where that is.
And you have a %r computer.  Nice.
""" % (likes, lives, computer)