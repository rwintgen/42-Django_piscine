def create_tuple():
	d = [
		('Hendrix' , '1942'),
		('Allman' , '1946'),
		('King' , '1925'),
		('Clapton' , '1945'),
		('Johnson' , '1911'),
		('Berry' , '1926'),
		('Vaughan' , '1954'),
		('Cooder' , '1947'),
		('Page' , '1944'),
		('Richards' , '1943'),
		('Hammett' , '1962'),
		('Cobain' , '1967'),
		('Garcia' , '1942'),
		('Beck' , '1944'),
		('Santana' , '1947'),
		('Ramone' , '1948'),
		('White' , '1975'),
		('Frusciante', '1970'),
		('Thompson' , '1949'),
		('Burton' , '1939')
	]

	return d

def print_dict(dict):
	# for year in dict:
	# 	print(f"{year} : {' '.join(dict[year])}")
	for year, names in dict.items():
		print(f"{year} : {' '.join(names)}")

def convert_to_dict():
	original = create_tuple()
	result = {}

	for name, year in original:
		if year not in result:
			result[year] = [name]
		else:
			result[year].append(name)

	print_dict(result)

if __name__ == '__main__':
    convert_to_dict()