import random

def ask_for_float(question: str) -> float:
	while True:
		answer: str = input(question).strip().lower()
		try:
			value: float = float(answer)
			return value
		except ValueError:
			print("Please enter a valid number")

def ask_yes_no(question: str) -> bool:
	while True:
		answer: str = input(question).strip().lower()
		if answer == "yes" or answer == "y":
			return True
		elif answer == "no" or answer == "n":
			return False
		else:
			print("Please enter a valid answer")

def main() -> None:
	money: float = ask_for_float("Enter money amount: ") # Probably should not use floats for money but...
	rounds: int = 0
	print()
	while True:
		if money <= 1.0:
			print(f"You dont have enough money to keep playing")
			break

		tokens: list[str] = ["unicorn", "zebra", "horse", "donkey"]
		weights: list[int] = [15, 25, 20, 40]
		amount: list[float] = [5.0, 0.5, 0.5, 0.0]

		index = random.choices([0, 1, 2, 3], weights=weights, k=1)[0]
		print(f"You got {tokens[index]}")
		print(f"You won ${amount[index]}")
		money += amount[index]

		money -= 1.0
		print(f"You have ${money} dollars left\n")
		rounds += 1
		
		if ask_yes_no("Do you want to quit? "):
			break
		else:
			print()

	print(f"You lasted {rounds} rounds")
	print("Goodbye")

if __name__ == "__main__":
	main()
