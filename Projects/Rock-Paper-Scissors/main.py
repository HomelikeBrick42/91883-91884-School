import random

def ask_yes_no(question: str) -> bool:
	while True:
		answer: str = input(question).strip().lower()
		if answer == "yes" or answer == "y":
			return True
		elif answer == "no" or answer == "n":
			return False
		else:
			print("Please enter a valid answer")

def ask_rock_paper_scissors() -> chr:
	while True:
		answer: str = input("Enter rock, paper or scissors: ").strip().lower()
		if answer == "rock" or answer == "r":
			return 'r'
		elif answer == "paper" or answer == "p":
			return 'p'
		elif answer == "scissors" or answer == "s":
			return 's'
		else:
			print("Please enter a valid answer")


def main() -> None:
	if ask_yes_no("Do you want to play first to 10? "):
		first_to_ten = True
	else:
		first_to_ten = False

	player_points: int = 0
	computer_points: int = 0
	while True:
		choices: dict[chr, str] = {
			'r': "rock",
			'p': "paper",
			's': "scissors",
		}

		player_choice: chr = ask_rock_paper_scissors()
		computer_choice: chr = random.choices(list(choices), k=1)[0]

		print(f"You chose {choices[player_choice]}")
		print(f"The computer chose {choices[computer_choice]}")

		wins: dict[chr, chr] = {
			'r': 's',
            'p': 'r',
            's': 'p',
		}

		looses: dict[chr, chr] = {
			'r': 'p',
            'p': 's',
            's': 'r',
		}

		if wins[player_choice] == computer_choice:
			print("You won!")
			player_points += 1
		elif looses[player_choice] == computer_choice:
			print("You loose!")
			computer_points += 1
		else:
			print("Tie!")

		print()
		if first_to_ten:
			print(f"You have {player_points} points.")
			print(f"The computer has {computer_points} points.")

			if player_points >= 10:
				print("You won!")
				break
			elif computer_points >= 10:
				print("You loose!")
				break
		else:
			if not ask_yes_no("Do you want to continue playing? "):
				break
		print()

	if not first_to_ten:
		print(f"You got {player_points} points.")
		print(f"The computer got {computer_points} points.")

if __name__ == "__main__":
	main()
