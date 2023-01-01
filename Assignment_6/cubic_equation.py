def cubic_equation(a, b, c, d):
    import cmath
    
    delta = 18*a*b*c*d - 4*((b**3)*d) + (b**2)*(c**2) - 4*((c**3)*a) - 27*((a**2)*(d**2))

    delta0 = (b**2) - 3*a*c
    delta1 = 2*(b**3) - 9*a*b*c + 27*(a**2)*d

    if delta == 0:
        if delta0 == 0:
            x = -b/(3*a)
            print("This equation has only one root")
            print("x = ", x)
        else:
            x0 = (9*a*d - b*c)/(2*delta0)
            x1 = (4*a*b*c - 9*(a**2)*d - b**3)/(a*delta0)
            print("This equation has two roots")
            print("x0 = ", x0)
            print("x1 = ", x1)

    else:
        m = ((delta1 + cmath.sqrt((delta1**2)-4*(delta0**3)))/2)**(1/3)
        u = [1 , (-1 + ((3**(0.5))*1j))/2 , (-1 - ((3**(0.5))*1j))/2]
        print("This equation has three roots")
        roots =[]

        for i in range(0,3):
            x = (-1/(3*a))* (b + u[i]*m + delta0/(u[i]*m))
            roots.append(x)

        for root in roots:
            if delta > 0:
                print("x = ", root.real)
            else:
                print("x = ", root)
  

while True:
    coefficients = list(map(int,input("Enter a, b, c and d: ").split()))
    a = coefficients[0]
    b = coefficients[1]
    c = coefficients[2]
    d = coefficients[3]
    print ("Your equation is :")
    print ("(", a, "x^3) +", "(", b, "x^2) +", "(", c, "x) +", d)
    if a != 0:
        cubic_equation(a, b, c, d)
        break
    else:
        print("You are not allowed to choose 0 for a")
