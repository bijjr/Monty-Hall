import random

def print_stats(win,loss):	
	win_perc = "%.2f" % (float(win / 1000))
	loss_perc = "%.2f" % (float(loss / 1000))

	print("Wins: {} \n{} percent of the time".format(win,win_perc))
	print("Losses: {} \n{} percent of the time".format(loss,loss_perc))

def switch_door(rd, sd):
	sd = 6 - rd - sd
	return sd

def remove_door(doors, pd, sd):
	pick = random.choice(doors)
	while pick == pd or pick == sd:
		pick = random.choice(doors)
	remove_door = pick
	return remove_door

def game():	
	win,loss = 0, 0
	for _ in range(1000):
		doors = [1,2,3]
		pd = random.choice(doors)
		print("prized door {}".format(pd))
		sd = random.choice(doors)
		print("selected door {}".format(sd))
		rd = remove_door(doors,pd,sd)
		print("removeddoor {}".format(rd))
		sd = switch_door(rd, sd)
		print("switched to door {}".format(sd))
		print("=========")
		if sd == pd:
			win += 1
		else:
			loss += 1
	print_stats(win,loss)	

def main():
	game()

if __name__ == '__main__':
	main()