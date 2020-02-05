import os
import platform

def clear():
	if (platform.system() == 'Windows'):
		os.system('cls')
	else:
		os.system('clear')
	return

def howTo():
	clear()

	print("Countdown is a game where we start off with 10 \
		\nand subtract 1, 2, or 3.  The objective is to force\
		\nthe other player to land on 0.  Have fun!\n \n ")
		
	return
	
userCharacter = 'y'

print("Welcome to Countdown!\n")

while ( userCharacter == 'y'):

	gameNumber = 10
	
	while ( gameNumber > 0):
	
		howTo()
		userNumber = 0
		print "Current Number: ", gameNumber
		
		#Error checking while loop, makes sure input is either 1,2, or 3
		while ( userNumber == 0):
		
			userNumber = int(input("Enter a 1,2,3: "))
			if userNumber <= 0 or userNumber > 3:
				print("Invalid number, please try again")
				userNumber = 0
				
		gameNumber -= userNumber
		
		if (gameNumber <= 0):
			print("You Lost")
			userCharacter = raw_input("To play again, enter 'y': ")
	

