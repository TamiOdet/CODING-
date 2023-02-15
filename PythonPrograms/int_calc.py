print ("(M)ultiplication, (S)ubtraction, (A)ddition, (D)ivision,")
userC = str(input("please select an operation: "))
int_1 = int(input("please provide the 1st integer:"))
int_2 = int(input("please provide the 2nd integer:" ))

multi = int_1 * int_2
add = int_1 + int_2
sub = int_1 - int_2 
div = int_1//int_2


if userC == "M":
	print (int_1, "x" ,int_2, "=" ,multi)
if userC == "A":
	print (int_1, "+" ,int_2, "=" ,add)
if userC == "S":
	print (int_1, "-" ,int_2, "=" ,sub)
if userC == "D":
	print (int_1, "/" ,int_2, "=" ,div)
else:
	print("please input a valid operation")
