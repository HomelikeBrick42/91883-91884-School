import random

from collections import Counter

def ask_for_int(question: str) -> int:
	while True:
		answer: str = input(question).strip().lower()
		try:
			value: int = int(answer)
			return value
		except ValueError:
			print("Please enter a valid integer")

def has_all_letters(tokens: list[chr], word: str) -> bool:
    return Counter(word) & Counter(tokens) == Counter(word)

def main() -> None:
	count: int = ask_for_int("How many times do you want to get the averge for? ")
	all_iterations: list[int] = []
	print()

	high_iterations: int = -float('inf')
	low_iterations: int = float('inf')
	for i in range(0, count):
		chars: list[chr] = ['c', 'o', 'f', 'e']
		tokens: list[chr] = []

		iterations: int = 0
		while not has_all_letters(tokens, "coffee"):
			tokens.append(random.choice(chars))
			print(f"Chose '{tokens[len(tokens) - 1]}'")
			iterations += 1
		
		print(f"Got the word coffee in {iterations} iterations")
		all_iterations.append(iterations)
		if iterations > high_iterations:
			high_iterations = iterations
		if iterations < low_iterations:
			low_iterations = iterations
		print()

	average_iterations: float = 0.0
	for it in all_iterations:
		average_iterations += float(it)
	average_iterations /= float(len(all_iterations))
	print(f"Average iterations: {average_iterations}")
	print(f"High iterations: {high_iterations}")
	print(f"Low iterations: {low_iterations}")

if __name__ == "__main__":
	main()
