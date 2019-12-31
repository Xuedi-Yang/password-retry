password = 'a123456' 
i = 3
while True:
	pwd = input('Please enter your pin:')
	if pwd == password:
		print('You have successfully entered!')
		break
	else:
		i = i - 1
		print('Wrong Pin!还有',i,'次机会')
		if i == 0:
			break
