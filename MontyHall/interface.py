#interface.py

import os
import random
import statistics

# [random.choice(door) for i in range(1000)]

# print("")
# print("")
# print("")
# print("")
# print("")

def play_again():
	goodbyes = ["Adios!","Goodbye!","Au Revoir!"]
	print("Would you like to play again?")
	print("\n")
	print("1. Yes")
	print("\n")
	print("2. No")
	play = int(input("> "))
	if play == 1:
		main()
	else:
		print(random.choice(goodbyes))
		exit()

def win_or_lose(user_choice, answer,doors):
	if user_choice == answer:
		print("V")
		print("\n")
		print("R")
		print("\n")
		print("O")
		print("\n")
		print("O")
		print("\n")
		print("M")
		print("\n")
		print("!")
		print("y o u w o n ! ! ! ! ! !  !")
	else:
		print("You lost! the car was behind door {}".format(answer))
		print(" have fun with the goat")
	clear()
	play_again()

def user_second_choice(user_choice,answer,door):
	if user_choice == answer:
		print("You've chosen door {}".format(user_choice))
		print("\n")
		print(".....")
		clear()
		win_or_lose(user_choice,answer,doors)
	else:
		print("You've chosen door {}".format(user_choice))
		print("\n")
		print("......")
		clear()
		win_or_lose(user_choice,answer,doors)

def user_first_choice(user_choice,answer,doors):
	if user_choice == answer:
		print("You've chosen door {}".format(answer))
		print("\n")
		print("Nice you got it on the first try!")
		exit()
	else:
		print("You've chosen door {}".format(user_choice))
		print("\n")
		print("Would you like to keep your choice or choose the other door?")
		print("1. Keep answer")
		print("2. Choose other door")
		user_choice = int(input("> "))
		clear()
		user_second_choice(user_choice, answer, doors)
		# return xyz(3)

def clear():
	return os.system('clear')

def main():
	print("")	
	old_doors = [1,2,3]
	answer = random.choice(old_doors)
	user_choice = int(input("> "))
	
	doors = list(filter(lambda x: x != answer, old_doors))

	user_first_choice(user_choice,answer,doors)

	play_again()


if __name__ == '__main__':
	main()

