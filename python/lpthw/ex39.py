﻿# -*- encoding:utf-8 -*-

states = {
    'Oregon' : 'OR',
    'Florida' : 'FL',
    'California' : 'CA',
    'New York' : 'NY',
    'Michigan' : 'MI'
}

cities = {
    'CA' : 'San Fransisco',
    'MI' : 'Detroit',
    'FL' : 'Jacksonville'
}

cities['NY'] = 'New York'
cities['OR'] = 'Portland'

print '--' * 10
print 'NY state has :', cities['NY']
print 'OR state has :', cities['OR']

print '--' * 10
print 'Michigan\'s abbreviation is :', states['Michigan']

print '--' * 10
print 'Michigan has city:', cities[states['Michigan']]

print '--' * 10
for state, abbrev in states.items():
    print '%s:%s' %(state,abbrev)

for abbrev, state in cities.items():
    print '%s:%s' %(abbrev, state)
