import os
import platform

def clear():
	if (platform.system() == 'Windows'):
		os.system('cls')
	else:
		os.system('clear')


def howTo():
	print("Countdown is a game where we start off with 10 \
		\nand subtract 1, 2, or 3.  The objective to force\
		\nthe other player to land on 0.  Have fun!\n \n ")

userCharacter = "a"

print("Welcome to Countdown!\n")

while ( userCharacter == "a"):

	gameNumber = 10
	
	while ( gameNumber > 0):
	
		howTo()
		print("Current Number: ", gameNumber)
		
		userNumber = int(input("Enter a 1,2,3: "))
		gameNumber -= userNumber
		
		if (gameNumber <= 0):
			print("You Lost")
			userCharacter = input("To play again, enter 'a': ")
		
		clear()
	

