import sys

def parse_file():
	table = {}
	
	with open("periodic_table.txt", "r") as f:
		for line in f:
			line = line.strip()

			elem_data = []
			name, attributes = line.split(" = ")
			attributes = attributes.split(", ")

			for attr in attributes:
				attribute_value = attr.split(":")[1]
				elem_data.append(attribute_value.strip())

			table[name] = tuple(elem_data)

	# for name, data in table.items():
	# 	print(f"{name}, {data}")

	return table

# def create_html():

if __name__ == '__main__':
	table = parse_file()
	# create_html(table)