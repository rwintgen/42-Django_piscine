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

def match_states_to_capitals():
	states, capitals = get_dicts()
	matched = dict()

	for state, symbol in states.items():
		capital = capitals[symbol]
		matched[state] = capital
	
	return matched

def find_capital(state):
	matched = match_states_to_capitals()
	if state in matched:
		return matched[state]
	else:
		return "Unknown state"

if __name__ == '__main__':
	if len(sys.argv) == 2:
		print(find_capital(sys.argv[1]))
	