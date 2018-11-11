while True:
	num = input('\nPlease enter a number, and I will tell you if it is even: ')

	num = int(num)
	if num != 0:
		if num % 2 == 0 and num % 4 == 0:
			print('Your number is even, and a multiple of 4')
		elif num % 2 == 0:
			print('Your number is even.')
		elif num % 2 == 1:
			print('Your number is odd.')
		else:
			print('Please try again.')
	elif num == 0:
		print('Please enter a nonzero number.')

	check = input('\nPlease provide a second number.: ')

	check = int(check)

	if num % check == 0:
		print(str(check) + ' divides evenly into ' + str(num) + '!')
	elif num % check != 0:
		print(str(check) + ' does not divide evenly into ' + str(num) + '.')
