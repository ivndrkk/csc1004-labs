class Meeting:
    def __init__(self, hour, minute, duration):
        self.hour = hour
        self.minute = minute
        self.duration = duration
    def __str__(self):
        return f"{self.hour:02d}:{self.minute:02d} ({self.duration} minutes)"
    
class Schedule:
    def __init__(self):
        self.meetings = []
    def add(self, meeting):
        self.meetings.append(meeting)
    def __str__(self):
        print("Schedule")
        print("--------")
        list_of_meetings = []
        for x in self.meetings:
            list_of_meetings.append(str(x))
        list_of_meetings.sort()
        list_of_meetings.append("Meetings today: " + str(len(self.meetings)))
        return "\n".join(list_of_meetings)