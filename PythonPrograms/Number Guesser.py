#Tami Odetoyinbo

def main():
	
	import random
	# ask user for random value between (1,100)
	print("Im thinking of a number between 1 and 100. ")

	value = random.randint(0,101)
	# ask user to guess any value between interval given
	num = int(input("Can you guess it?"))

	left_over = value - num
	# if value isnt the same, tell user how many numbers away both numbers were from each other
	if value != num:
		print ("you were", abs(left_over),"away!")
	else:
		print ("good job! you chose the same number.")
#ask user if they would like to repeat
	restart = input("would you like to restart?")
	if restart == 'yes':
		main()
	else:
		exit()
main()