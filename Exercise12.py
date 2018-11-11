def first_and_last():
	numbers_list = []

	length = input('Please tell me how long you would like your list: ')
	length = int(length)

	for i in range(length):
		num = input('Please enter a number you would like to add to your list: ')
		numbers_list.append(num)
		
	print('The list you have chosen is ' + str(numbers_list) + '.\n')

	print('The first element of your list is ' + numbers_list[0] + '.')
	print('The last element of your list is ' + numbers_list[-1] + '.')

	new_list = [numbers_list[0], numbers_list[-1]]
	print('\nYour new list consisting of these two numbers is ' + str(new_list) + '.')

first_and_last()
