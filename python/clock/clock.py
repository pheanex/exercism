class Clock(object):
    def __init__(self, hour, minute):
        self.minutes = minute
        self.hours = hour

    def __add__(self, minutes):
        self.minutes += minutes
        return self

    def __eq__(self, other):
        self_hour, self_minute = divmod(self.minutes, 60)
        self_hour = (self.hours + self_hour) % 24
        other_hour, other_minute = divmod(other.minutes, 60)
        other_hour = (other.hours + other_hour) % 24
        return (self_hour, self_minute) == (other_hour, other_minute)

    def __str__(self):
        hour, minute = divmod(self.minutes, 60)
        hour = (self.hours + hour) % 24
        return '{0:02d}:{1:02d}'.format(hour, minute)
