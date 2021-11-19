'''Rye Ledford - Computer Science - Lab 11'''

import time

class clock:
    def __init__(self, hour, minutes, seconds, day_nite):
        self.hour = hour
        self.minutes = minutes
        self.seconds = seconds
        self.day_nite = day_nite
        if day_nite == 1:
            if self.hour > 12:
                self.hour += 12
        return 

   

    def __str__(self):
        if self.day_nite == 0:
            return '{:02}:{:02}:{:02}'.format(self.hour, self.minutes, self.seconds)
        
        elif self.day_nite == 1:
            if self.hour <= 11:
                return "{:02}:{:02}:{:02} am".format(self.hour, self.minutes, self.seconds)
            else:
                return "{:02}:{:02}:{:02} pm".format(self.hour, self.minutes, self.seconds)
         
        else:
            print('Not a valid clock type, please enter 0 for a twelve hour clock or 1 for a twenty four hour clock')


    def tick(self):
        self.seconds += 1
        if self.seconds == 60:
            self.seconds = 0
            self.minutes += 1
        else:
            if self.minutes == 60:
                self.minutes = 0
                self.hour += 1
            else:
                if self.hour == 12:
                    self.hour = 0
                else:
                    return

'''hour = int(input('What is the current hour ==> '))
minutes = int(input('What is the current minute ==> '))
seconds = int(input('What is the current second ==> '))
day_nite = 0
clock = clock(hour, minutes, seconds, day_nite)
i = 0
while i<45:
    print(clock)
    clock.tick()
    i += 1
    time.sleep(1)'''
