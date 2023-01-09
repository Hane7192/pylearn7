class My_Time:
    def __init__(self, hour, minute):
        self.h = hour
        self.m = minute

    def time_to_min(self):
        result = self.h*60 + self.m
        return result