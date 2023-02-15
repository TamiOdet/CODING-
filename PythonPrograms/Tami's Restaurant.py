#restaurant to order doughnuts, user can purchase any items from the menu, will be given
#total and can have payment converted from usd or euros to cad. user will be given receipt at the end
print("Welcome, to Tami's International Doughnut Shoppe!")
b = 1 #this is just a random assignment used to access the while loop
x = 0
opt_1 = 3.50 
opt_2 = 2.25 
opt_3 = 4.05
opt_4 = 1.99 

total = 0
total_1 = 0
total_2 = 0
total_3 = 0
total_4 = 0
num = 0

option_1 = ""
option_2 = ""
option_3 = ""
option_4 = ""

CAD = 1
EUR = 0.70
USD = 0.75


name = input("Please enter your name to begin: ")

print(" ")

print("Please select a doughnut from the following menu: ")

print("1. Chocolate-dipped Maple Puff ($3.50 each) ")
print("2. Strawberry Twizzler ($2.25 each) ")
print("3. Vanilla Chai Strudel ($4.05 each) ")
print("4. Honey-drizzled Lemon Dutchie ($1.99 each) ")
print("5. No more doughnuts.")

y = int(input("> "))

while (b == 1):
 
	if (y < 0 or y > 5):
		print("I'm sorry, that is not a valid selection. Please enter a selection from 1-5. ")
		
		print("1. Chocolate-dipped Maple Puff ($3.50 each) ")
		print("2. Strawberry Twizzler ($2.25 each) ")
		print("3. Vanilla Chai Strudel ($4.05 each) ")
		print("4. Honey-drizzled Lemon Dutchie ($1.99 each) ")
		print("5. No more doughnuts.")
		y = int(input("> "))
	else:
		break

while(y != 5):
	
	if (y == 1):
		num = int(input("How many Chocolate-dipped Maple Puffs would you like to purchase? "))
		total_1 = num * opt_1
		option_1 = str(num) + " Chocolate-dipped Maple Puffs"
		
		
		
	elif (y == 2):
		num = int(input("How many Strawberry Twizzlers would you like to purchase? "))
		total_2 = num * opt_2	
		option_2 = str(num) + " Strawberry Twizzlers"
		
		
		
	elif (y == 3):
		num = int(input("How many Vanilla Chai Strudels would you like to purchase? "))
		total_3 = num * opt_3
		option_3 = str(num) + " Vanilla Chai Strudels"
		
		
		
	else:
		num = int(input("How many Honey-drizzled Lemon Dutchies would you like to purchase? "))
		total_4 = num * opt_4
		option_4 = str(num) + " Honey-drizzled Lemon Dutchies"
		
		
	print("Please select a doughnut from the following menu: ")

	print("1. Chocolate-dipped Maple Puff ($3.50 each) ")
	print("2. Strawberry Twizzler ($2.25 each) ")
	print("3. Vanilla Chai Strudel ($4.05 each) ")
	print("4. Honey-drizzled Lemon Dutchie ($1.99 each) ")
	print("5. No more doughnuts.")
	y = int(input("> "))
	
total = total_1 + total_2 + total_3 + total_4

print("What currency will you be paying with?")
print("1. CAD")
print("2. EUR")
print("3. USD") 
x = int(input("> "))

if (x == 1):
	new_total = total * CAD
	curr = "(CAD)"
elif (x == 2):
	new_total = total * EUR
	curr = "(EUR)"
elif (x == 3):
	new_total = total * USD
	curr = "(USD)"
	
new_total = format(new_total, '.2f')

print (name + ", here is your receipt:")
print ("---------------------------------------")
print (option_1 + '\n' + option_2 + '\n' + option_3 + '\n' + option_4)
print ("-----------------------------------------")
print ("Total cost: " ,new_total, curr)
print ("Thank you, have a nice day!")
