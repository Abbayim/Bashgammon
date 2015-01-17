from board import Board
import random
import sys

#todo: jail rolls
#todo: can't split dice rolls
#todo: make sure the "done" thing works
exitTerms = ("quit", "exit", "bye","q")
def main():
	b = Board()
	intro = open('readme.txt', 'r')
	
	SIDE = True #True if X, false if O
	for line in intro:
		print(line)
	print("What do you want to play? Type 'pc' for Player vs. Computer or 'pp' for Player vs. Player")

	line = input()
	if line == 'pc':
		print("I haven't done this yet!")
	else:
		while (line not in exitTerms and (b.xFree < 15 or b.oFree < 15)):
			print(b)
			roll1 = random.randint(1,6)
			roll2 = random.randint(1,6)
			turnComplete = False
			total = roll1 + roll2
			if (roll1 == roll2):
				total *= 2
			print("You rolled a " + str(roll1) + " and a " + str(roll2) + " giving you a total of " + str(total) + " moves.")
			if SIDE:
				print("X, what do you want to do?")
			else:
				print("O, what do you want to do?")
			while (not turnComplete and line not in exitTerms and total > 0):
				line = input()
				space,steps = parseInput(line)
				jailFreed = False
				jailCase = False
				if (SIDE and b.xJail > 0):
					jailCase = True
				if (not SIDE and b.oJail > 0):
					jailCase = True
				if (space == 100 and steps == 100):
					total = 0
					break
				if (space == 101 and steps == 101):
					break
				if (steps != roll1 and steps != roll2 and steps != (roll1 + roll2) and steps != 100 and not jailCase):
					print("You didn't roll that!")
					continue
					# Must jump to beginning of loop
				space = space - 1
				if (steps == 0 and SIDE and b.xJail > 0):
					tempSteps = space - 18
					if (tempSteps != roll1 and tempSteps != roll2):
						print("You didn't roll that!")
						continue
					else:
						jailFreed = True
				elif (steps == 0 and not SIDE and b.oJail > 0):
					tempSteps = space + 1
					if (tempSteps != roll1 and tempSteps != roll2):
						print("You didn't roll that!")
						continue
					else:
						jailFreed = True
				if (space < 0 or space > 23 or steps < 0):
					print("That move is not allowed.  Please try again.")
					continue
					#Same deal here.
				move, response = b.makeMove(space, SIDE, steps)
				print(response)
				if (move and jailFreed):
					steps = tempSteps
				if move:
					total = total - steps
					print(b)
					print("You have " + str(total) + " steps left.")
			SIDE = not SIDE


#TODO: Include error management
def parseInput(response):
	if response == "d" or response == "f" or response == "done" or response == "finish":
		return(100,100)
	if response in exitTerms:
		return (101, 101)
	# if type(response) == type("Sample string"):
	# 	return(101,101)
	loc = findSeparation(response)
	return(int(response[:loc]), int(response[loc+1:])) 

def findSeparation(value):
	for i in range(len(value)):
		if (value[i] == ' ' or value[i] == ','):
			return i
	return 0

if __name__ == "__main__":
	main()