import math

class Fraction:
    
    #properties
    def __init__(self, numerator, denominator):
        
        self.n = numerator
        self.d = denominator
    
    #methods
    def sum(self, other):
        result_n = self.n * other.d + self.d * other.n
        result_d = self.d * other.d

        result = Fraction(result_n, result_d)
        return result
        

    def mul(self, other):
        result_n = self.n * other.n
        result_d = self.d * other.d

        result = Fraction(result_n, result_d)
        return result

    def sub(self, other):
        result_n = self.n * other.d - self.d * other.n
        result_d = self.d * other.d

        result = Fraction(result_n, result_d)
        return result

    def div(self, other):
        result_n = self.n * other.d
        result_d = self.d * other.n

        result = Fraction(result_n, result_d)
        return result

    def fraction_to_number(self):
        result = self.n / self.d

        return result

    def simplify(self):
        gcd = math.gcd(self.n, self.d)
        result_n = int(self.n / gcd)
        result_d = int(self.d / gcd)
        result = Fraction(result_n, result_d)

        return result

    def show(self):
        print(self.n, "/", self.d)

while True:

    print("Enter + to add two Fractions ")
    print("Enter - to subtract the second fraction from the first one ")
    print("Enter * to multiply two Fractions ")
    print("Enter / to divide the first fraction by the second one ")
    print("Enter num to show the fraction as a float number ")
    print("Enter sim to simplify the fraction if it is possible ")
    print("Enter esc to quit")
    
    operator = input("Choose your operator: ")

    if operator == "esc":
        break

    elif operator == "num" or operator == "sim":
        a = list(map(int,input("Enter numerator and denominator of the first fraction with a space in between: ").split(" ")))
        frac = Fraction(a[0] , a[1])
        frac.show()

        if operator == "num":
            float_num = frac.fraction_to_number()
            print("The result is: ", float_num)

        elif operator == "sim":
            simplified_frac = frac.simplify()
            print("The result is: ")
            simplified_frac.show()
    else:
        
        a = list(map(int,input("Enter numerator and denominator of the first fraction with a space in between: ").split(" ")))
        frac_1 = Fraction(a[0] , a[1])
        frac_1.show()

        b = list(map(int,input("Enter numerator and denominator of the first fraction with a space in between: ").split(" ")))
        frac_2 = Fraction(b[0] , b[1])
        frac_2.show()

        if operator == "+":
            summation = frac_1.sum(frac_2)
            print("The result is: ")
            summation.show()

        elif operator == "-":
            subtraction = frac_1.sub(frac_2)
            print("The result is: ")
            subtraction.show()

        elif operator == "*":
            multiply = frac_1.mul(frac_2)
            print("The result is: ")
            multiply.show()

        elif operator == "/":
            division = frac_1.div(frac_2)
            print("The result is: ")
            division.show()
