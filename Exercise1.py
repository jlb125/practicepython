name = input('Please enter your name: ')
age = input('Please enter your age: ')

age = int(age)

remainingyears = 100 - age
year = 2018 + remainingyears

message ='You will turn 100 years old in year ' + str(year) + '.'

print(message)

count = input('\n\nPlease enter the number of times you would like this message repeated: ')

count = int(count)

for i in range(count):
	print('\n' + message)
