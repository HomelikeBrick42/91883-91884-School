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

def ask_for_int(question: str) -> int:
	while True:
		answer: str = input(question).strip().lower()
		try:
			value: int = int(answer)
			return value
		except ValueError:
			print("Please enter a valid integer")

def show_instructions() -> None:
	print("----- How To Play -----")
	print("A number between 1 and 100 will be chosen")
	print("You have 7 guesses")
	print("You have to gess a number and the program will say higher or lower")
	print("Then you know if you need to go higher or lower for your guess")
	print("If you guess the number you win!")

def main() -> None:
	if not ask_yes_no("Do you know how to play? "):
		show_instructions()
	print()

	secret: int = random.randint(1, 100)

	guess: int = -1
	best_guess: int = -1
	best_guess_difference: int = -1

	guesses: int = 0
	while True:
		guess = ask_for_int("Enter your guess: ")

		if guess < secret:
			print("Higher")
		elif guess > secret:
			print("Lower")
		else:
			print("You found the secret number!")
			return

		if abs(guess - secret) < best_guess_difference or best_guess == -1:
			best_guess_difference = abs(guess - secret)
			best_guess = guess

		guesses += 1
		if guesses >= 9:
			print("You are out of guesses")
			print(f"The secret was {secret}")
			print(f"Your best guess was {best_guess}")

if __name__ == "__main__":
	while True:
		main()
