
print ("Enter the two positive integer numbers : ")
a = int (input ())
b = int (input ())

for i in range (1, a + 1):
	if i <= b:
		if a % i == 0 and b % i == 0:
			gcd = i

print ("The GCD of ", a, " & ", b, " is: ", gcd)