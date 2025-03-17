def parse_csv():
	f = open("numbers.txt", "r")
	content = f.read()
	numbers = content.split(",")
	return numbers

def print_numbers():
	numbers = parse_csv()
	for num in numbers:
		print(num)

if __name__ == '__main__':
	print_numbers()
