# -*- encoding:utf-8 -*-

# Modules, Classes, Objects


# module example: mystaff module
import mystaff
mystaff.apple()
print mystaff.tangerine

class Song(object):
    
    def __init__(self, lyrics):
        self.lyrics = lyrics
    
    def sing_me_a_song(self):
        for line in self.lyrics:
            print line


happy_birthday = Song(["Happy","Birthday","to u"])
happy_birthday.sing_me_a_song()



from mystaff import MyStaff

# playing with class
thing = MyStaff()
thing.apple()
print thing.tangerine









