import os

import random
random.seed = os.urandom(1)[0]

from typing import Union

def ask_for_int(question: str, min: Union[int, None] = None, max: Union[int, None] = None) -> int:
	while True:
		answer: str = input(question).strip().lower()
		try:
			value: int = int(answer)
			if min != None and value < min:
				print(f"Please enter a integer greater than {min-1}")
				continue
			if max != None and value > max:
				print(f"Please enter a integer less than {max+1}")
				continue
			return value
		except ValueError:
			print("Please enter a valid integer")
			continue

def main() -> None:
	player_car: int = ask_for_int("Chose a car between 1 and 6: ", min=1, max=6)

	race_distance: int = ask_for_int("Enter race distance between 5 and 15: ", min=5, max=15)

	computer_choice: list[int] = [1, 2, 3, 4, 5, 6]
	computer_choice.remove(player_car) # The computer could have the same car as the player
	computer_car: int = random.choice(computer_choice)
	print('\n')

	print(f"You chose car {player_car}")
	print(f"The computer chose car {computer_car}")
	print(f"The race distance is {race_distance}")
	print('\n')

	player_distance: int = 0
	computer_distance: int = 0
	while player_distance < race_distance and computer_distance < race_distance:
		move: int = random.randint(0, 6)
		if move == player_car:
			player_distance += 1
			print("You have moved by 1")
			print(f"You are at {player_distance}\n")
		elif move == computer_car:
			computer_distance += 1
			print("The computer has moved by 1")
			print(f"The computer is at {computer_distance}\n")

	if player_distance == race_distance:
		print("You won!")
	elif computer_distance == race_distance:
		print("You loose!")
	else:
		assert(False) # We should never get here

if __name__ == "__main__":
	main()
