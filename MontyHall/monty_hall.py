import os
import random
import statistics

# def run_again():
# 	run = int(input("Would you like to simulate again? "))
# 	if run == 1:
# 		main()
# 	else:
# 		exit()

def print_stats(win,loss):
	
	win_percentage = "%.2f" % (float(win / 1000))
	lose_percentage = "%.2f" % (float(loss / 1000))

	print("You won {} percent of the time".format(win_percentage))
	print("and lost {} percent of the time".format(lose_percentage))


def game():	

	win,loss = 0, 0
	for i in range(1000):
		doors = [1,2,3]
		prize_door = random.choice(doors)
		select_door = random.choice(doors)
		p = random.choice(doors)
		while p == prize_door or p == select_door:
			p = random.choice(doors)
		remove_door = p
		#switch_door
		# select_door = 6 - remove_door - select_door
		
		print(prize_door)
		print(select_door)
		print(remove_door)
	
		if select_door == prize_door:
			win += 1
		else:
			loss += 1

	print("you loss {} times".format(win))
	print("you loss {} times".format(loss))

	print_stats(win,loss)

def main():
	game()
	# run_again()


if __name__ == '__main__':
	main()

