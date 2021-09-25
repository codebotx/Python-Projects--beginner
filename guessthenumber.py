import random
def guess(x):
	random_number =random.randint(1,x)
	guess=0

	while (guess!=random_number):
		guess=int(input(f"Guess a number between 1 and {x}:  "))
		if(guess<random_number):
			print('Guess again. Too Low!')
		elif(guess>random_number):
			print('Guess again. Too High!')
		print(guess)
	print("Yay, congrats. Hou have guessed the number, random number! {}".format(random_number))

# guess(10)

def computer_guess(x):
	low=1
	high=x
	feedback=''
	while feedback!= 'c':
		if  low!=high:
			guess=random.randint(low,high)
		else:
			guess=high
		feedback=input(f'Is {guess} too high (H), loo low, (L) or correct (C)?'.lower())
		if(feedback=='h'):
			high=guess-1
		elif(feedback=='l'):
			low=guess+1
	print(f'Yay! The computer guess your number, {guess}, corectly!')

# computer_guess(10)
