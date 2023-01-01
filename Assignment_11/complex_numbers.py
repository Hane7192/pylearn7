class Complex:
    def __init__(self, real, imaginery):
        self.r = real
        self.i = imaginery

    def show(self):
        if self.i >= 0:
            print(self.r, "+", self.i, "i")
        else:
            print(self.r, "-", abs(self.i), "i")

    def sum(self, other):
        real = self.r + other.r
        imaginery = self.i + other.i
        result = Complex(real, imaginery)

        return result

    def sub(self, other):
        real = self.r - other.r
        imaginery = self.i - other.i
        result = Complex(real, imaginery)

        return result

    def mul(self, other):
        real = self.r * other.r - self.i * other.i
        imaginery = self.r * other.i + self.i * other.r
        result = Complex(real, imaginery)

        return result


while True:

    print("Enter + to add two complex numbers ")
    print("Enter - to subtract the second complex number from the first one ")
    print("Enter * to multiply two complex numbers ")
    print("Enter esc to quit")

    operator = input("Choose your operator: ")

    if operator == "esc":
        break
    
    else:
        a = list(map(int,input("Enter real and imaginery parts of the first complex number with a space in between: ").split(" ")))
        comp_1 = Complex(a[0] , a[1])
        comp_1.show()

        b = list(map(int,input("Enter real and imaginery parts of the second complex number with a space in between: ").split(" ")))
        comp_2 = Complex(b[0] , b[1])
        comp_2.show()
        
        if operator == "+":
            sum = comp_1.sum(comp_2)
            print("The result is: ")
            sum.show()

        elif operator == "-":
            sub = comp_1.sub(comp_2)
            print("The result is: ")
            sub.show()
            
        elif operator == "*":
            mul = comp_1.mul(comp_2)
            print("The result is: ")
            mul.show()