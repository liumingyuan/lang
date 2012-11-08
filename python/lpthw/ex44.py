# -*- encoding:utf-8 -*-

class Parent(object):
    
    def __init__(self):
        print "Parent init()"
    
    def implicit(self):
        print "Parent Implicit()"
    
    def override(self):
        print "Parent override()"
    
    def altered(self):
        print "Parent Altered"
    
    

class Child(Parent):
    
    def override(self):
        print "Child override()"
    
    def altered(self):
        print "Child before altered()"
        super(Child, self).altered()
        print "Child after altered()"
    
    def __init__(self, stuff):
        self.stuff = stuff
        super(Child, self).__init__()
    


dad = Parent()
son = Child("cool")

dad.implicit()
son.implicit()

dad.override()
son.override()

dad.altered()
son.altered()







