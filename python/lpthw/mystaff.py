# -*- encoding : utf-8 -*-

# used to demostrate module class and create object
# ex40.py

def apple():
    print "IamAPPLE in module"

tangerine = "tangerine in module"


class MyStaff(object):
    
    def __init__(self):
        self.tangerine = " tangerine in class"
    
    def apple(self):
        print "classy apple"