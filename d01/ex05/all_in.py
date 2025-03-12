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

def handle_input(expressions):
	formatted_expressions = dict()

	for expr in expressions:
		expr = expr.strip()
		type_expr = find_type(expr.title())

		key = expr.title() if type_expr else expr
		formatted_expressions[key] = type_expr
	
	return formatted_expressions

def find_type(expression):
	states, capitals = get_dicts()

	if expression in states.keys():
		return "state"
	elif expression in capitals.values():
		return "capital"
	else:
		return 0
	
def pair_states_and_capitals(expressions):
	states, capitals = get_dicts()

	for expr, type in expressions.items():
		if expr == "":
			continue
		
		if type == "state":
			print(f"{find_capital(expr, states, capitals)} is the capital of {expr}")
		elif type == "capital":
			print(f"{expr} is the capital of {find_state(expr, states, capitals)}")
		else:
			print(f"{expr} is neither a capital city nor a state")

def find_capital(expr, states, capitals):
	matched = dict()

	for state, symbol in states.items():
		capital = capitals[symbol]
		matched[state] = capital
	
	return matched[expr]

def find_state(expr, states, capitals):
	matched = dict()

	for symbol, capital in capitals.items():
		state_name = next((state for state, abbrev in states.items() if abbrev == symbol), None)
		matched[capital] = state_name

	return matched[expr]

if __name__ == '__main__':
	if len(sys.argv) == 2:
		expressions = handle_input(sys.argv[1].split(","))
		pair_states_and_capitals(expressions)