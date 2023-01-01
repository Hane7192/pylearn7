class Time:
    def __init__(self, hour, minute, second):
        self.h = hour
        self.m = minute
        self.s = second
        self.fix()

    def show(self):
        print("%.2d" % self.h, ":", "%.2d" % self.m, ":", "%.2d" % self.s)

    def sum(self, other):
        s_new = self.s + other.s
        m_new = self.m + other.m
        h_new = self.h + other.h
        result = Time(h_new, m_new, s_new)
        
        return result
    
    def sub(self , other):
        s_new = self.s - other.s
        m_new = self.m - other.m
        h_new = self.h - other.h
        result = Time(h_new, m_new, s_new)
        
        return result

    def time_to_sec(self):
        result = self.h*3600 + self.m*60 + self.s
        return result

    def GMT_to_IRT(self):
        teh_h = self.h + 4
        teh_m = self.m + 30
        teh_s = self.s
        result = Time(teh_h, teh_m, teh_s)

        return result

    def fix(self):
        if self.s >= 60:
            self.s -= 60
            self.m += 1

        if self.m >= 60:
            self.m -= 60
            self.h += 1

        if self.s < 0:
            self.s += 60
            self.m -= 1

        if self.m < 0:
            self.m += 60
            self.h -= 1

while True:

    print("Enter + to add two times ")
    print("Enter - to subtract the second time from the first one ")
    print("Enter t2s to convert time to seconds ")
    print("Enter s2t to convert seconds to time ")
    print("Enter GMT2IRT to convert Greenwich time to Iran Time ")
    print("Enter esc to quit")

    operator = input("Choose your operator: ")

    if operator == "esc":
        break
    
    elif operator == "s2t":
        seconds = int(input("Enter a positive integer: "))
        h = (seconds// 3600)
        m = ((seconds % 3600) // 60)
        s = ((seconds % 3600) % 60)
        time = Time(h, m, s)
        time.show()

    elif operator == "+" or operator == "-":
        a = list(map(int,input("Enter the first time in the format (h m s) with a space in between: ").split(" ")))
        time_1 = Time(a[0], a[1], a[2])
        time_1.show()

        b = list(map(int,input("Enter the second time in the format (h m s) with a space in between: ").split(" ")))
        time_2 = Time(b[0], b[1], b[2])
        time_2.show()
    
        if operator == "+":
            summation = time_1.sum(time_2)
            summation.show()

        elif operator == "-":
            subtraction = time_1.sub(time_2)
            print("The result is: ")
            subtraction.show() 

    else:
        a = list(map(int,input("Enter the time in the format (h m s) with a space in between: ").split(" ")))
        time = Time(a[0], a[1], a[2])
        time.show()

        if operator == "t2s":
            seconds = time.time_to_sec()
            print("is equal to: ", seconds, " seconds")

        elif operator == "GMT2IRT":
            IRT = time.GMT_to_IRT()
            IRT.show()



