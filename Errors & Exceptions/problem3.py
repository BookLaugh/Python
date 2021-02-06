from colorama import *
init()

def ask():

	point = True
	while point:
		try:
			print('')
			x = int(input("Pls provide an integer number: "))
			print('')
		except:
			print('')
			print(Fore.RED+'Error ! Pls try again !')
			continue
		else:
			print('Thank you for cooperation, the number squared is: {}'.format(x**2))
			point = False
ask()