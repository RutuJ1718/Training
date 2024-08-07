#Class Time to add time and display it:

class Time:
    def __init__(self, hours, minutes):
        self.hours = hours
        self.minutes = minutes
    
    def addTime(self, t):
        total_minutes = self.minutes + t.minutes
        total_hours = self.hours + t.hours + total_minutes // 60
        total_minutes = total_minutes % 60
        return Time(total_hours, total_minutes)
    
    def displayTime(self):
        print(f"{self.hours} hr and {self.minutes} min")
    
    def displayMinute(self):
        total_minutes = self.hours * 60 + self.minutes
        print(f"Total minutes: {total_minutes}")

t1 = Time(4, 50)
t2 = Time(3, 20)
t3 = t1.addTime(t2)

t3.displayTime()
t3.displayMinute()
