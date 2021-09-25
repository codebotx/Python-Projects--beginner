import random

def play():
	user=input("What's your choice 'r' for rock, 'p' for paper, and 's' for scissors\n")
	computer=random.choice(['r','p','s'])

	if user==computer:
		return 'Its a tie'
	
	if is_win(user,computer):
		return 'You won!'

	return 'You lost!'


def is_win(player,oppnent):
	if(player=='r' and oppnent=='s') or (player=='s' and oppnent=='p') or (player=='p' and oppnent=='r'):
		return True
	
print(play())