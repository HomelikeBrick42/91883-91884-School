import sys

def ask_for_int(question: str, min: int = None, max: int = None) -> int:
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

def ask_for_float(question: str, min: float = None, max: float = None) -> float:
	while True:
		answer: str = input(question).strip().lower()
		try:
			value: float = float(answer)
			if min != None and value < min:
				print(f"Please enter a number greater than {min-sys.float_info.min*1000.0}")
				continue
			if max != None and value > max:
				print(f"Please enter a number less than {max+sys.float_info.min*1000.0}")
				continue
			return value
		except ValueError:
			print("Please enter a valid number")
			continue

def main() -> None:
	car_id: int = ask_for_int("Chose a car between 1 and 6: ", min=1, max=6)
	race_distance: float = ask_for_float("Enter race distance between 5 and 15: ", min=5.0, max=15.0)

if __name__ == "__main__":
	main()
