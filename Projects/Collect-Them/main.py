import random

from collections import Counter

def has_all_letters(tokens: list[chr], word: str) -> bool:
    return Counter(word) & Counter(tokens) == Counter(word)

def main() -> None:
	chars: list[chr] = ['c', 'o', 'f', 'e']
	tokens: list[chr] = []

	iterations: int = 0
	while not has_all_letters(tokens, "coffee"):
		tokens.append(random.choice(chars))
		print(f"Chose '{tokens[len(tokens) - 1]}'")
		iterations += 1
	
	print(f"Got the word coffee in {iterations} iterations")

if __name__ == "__main__":
	main()
