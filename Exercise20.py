import random

list_len = input('Please enter your desired list length: ')
list_len = int(list_len)

list = []

for i in range(list_len):
	list.append(random.randint(0,100))

list = sorted(list)

print(list)

num = input('Please enter a number to see if it is in the list: ')
num=int(num)

if num in list:
	print('Your number is in the list!')
else:
	print('Sorry, your number is not in the list.')
