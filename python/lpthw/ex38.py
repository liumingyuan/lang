# -*- encoding:utf-8 -*-
ten_things = "Apples Oranges Crows Telephone Light Sugar"

print "Wait there's not 10 things in that list, let's fix that"
stuff = ten_things.split(' ')
more_stuff = ["day", "night", "song", "fris", "corn", "banan" ,"girl", "boyh"]

while len(stuff) != 10:
    next_one = more_stuff.pop()
    stuff.append(next_one)
    print "There's %d items now." % len(stuff)

print "There we go: " ,stuff

print "Let's do something with stuff"
print stuff[1]
print stuff[-1]
print stuff.pop()
print ' '.join(stuff)
print '$'.join(stuff)
