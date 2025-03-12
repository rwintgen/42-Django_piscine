import sys

def get_dicts():
	states = {
	"Oregon" : "OR",
	"Alabama" : "AL",
	"New Jersey": "NJ",
	"Colorado" : "CO"
	}

	capital_cities = {
	"OR": "Salem",
	"AL": "Montgomery",
	"NJ": "Trenton",
	"CO": "Denver"
	}

	return states, capital_cities

def match_capitals_to_states():
	states, capitals = get_dicts()
	matched = dict()

	for symbol, capital in capitals.items():
		state_name = next((state for state, abbrev in states.items() if abbrev == symbol), None)
		matched[capital] = state_name
	
	return matched

def find_state(capital):
	matched = match_capitals_to_states()
	if capital in matched:
		return matched[capital]
	else:
		return "Unknown capital city"

if __name__ == '__main__':
	if len(sys.argv) == 2:
		print(find_state(sys.argv[1]))
	