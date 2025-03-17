from beverages import HotBeverage, Coffee, Tea, Chocolate, Cappuccino
import random

class CoffeeMachine:
	def __init__(self):
		self.drinks_left = 10

	class EmptyCup(HotBeverage):
		price = 0.90
		name = "empty cup"
		description = "An empty cup?! Gimme my money back!"
	
	class BrokenMachineException(Exception):
		def __init__(self):
			super().__init__("This coffee machine has to be repaired.")
	
	def repair(self):
		self.drinks_left = 10

	def serve(self, drink: HotBeverage):
		if self.drinks_left <= 0:
			raise self.BrokenMachineException()

		self.drinks_left -= 1
		return random.choice([drink(), self.EmptyCup()])

def serve_until_breaks(coffee_machine):
	all_drinks = [Coffee, Tea, Chocolate, Cappuccino]

	for _ in range(11):
		beverage = random.choice(all_drinks)

		try:
			print(coffee_machine.serve(beverage))
		except coffee_machine.BrokenMachineException as e:
			print(e)
			return

def test():
	coffee_machine = CoffeeMachine()

	serve_until_breaks(coffee_machine)
	coffee_machine.repair()
	serve_until_breaks(coffee_machine)

if __name__ == '__main__':
	test()		