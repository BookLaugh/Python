def ask_for_it():
	while True:
		try:
			total = int(input('Pls type a number: '))
		except:
			print("Woops ! That's not a number")
			continue
		else:
			print('Thank you for cooperation:)')
			break
		finally:
			print('I will be always running here around to help you ')
ask_for_it()