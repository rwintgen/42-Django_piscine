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

def create_html(table):
	with open("periodic_table.html", "w") as f:
		f.write("""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Periodic Table</title>
    <style>
        table {
            border-collapse: collapse;
        }
        td {
            border: 1px solid black;
            text-align: center;
			width: 180px;
			height: 180px;
        }
        ul {
            padding: 0;
            list-style-type: none;
        }
    </style>
</head>
<body>
    <h1>Periodic Table of Elements</h1>
	<table>
		<tr>""")

		current_pos = 0
		first_line = True
		for name, (position, number, symbol, mass, electrons) in table.items():
			position = int(position)
			if position == 0 and first_line == False:
				current_pos = 0
				f.write("""
			</tr>
			<tr>\n""")
			first_line = False
				
			while current_pos < position:
				f.write("""
			<td></td>\n""")
				current_pos += 1

			f.write(f"""
			<td style="border: 1px solid black; padding: 10px;">
				<h4>{name}</h4>
				<ul>
					<li>No {number}</li>
					<li>{symbol}</li>
					<li>{mass}</li>
					<li>{electrons} electrons</li>
				</ul>
			</td>\n""")
			current_pos += 1
		
		f.write("""
		</tr>
	</table>
</body>
</html>""")

if __name__ == '__main__':
	table = parse_file()
	create_html(table)