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
		if not ask_yes_no("Do you want to continue playing? "):
			break
		print()

	print(f"You got {player_points} points.")
	print(f"The computer got {computer_points} points.")

if __name__ == "__main__":
	main()
