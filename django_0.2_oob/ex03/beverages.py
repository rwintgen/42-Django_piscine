class HotBeverage:
	price = 0.30
	name = "hot beverage"
	description = "Just some hot water in a cup."

	def decription(self):
		return self.decription

	def __str__(self):
		return f"name : {self.name}\nprice : {self.price:.2f}\ndescription : {self.description}"
	
class Coffee(HotBeverage):
	price = 0.40
	name = "coffee"
	description = "A coffee, to stay awake."

class Tea(HotBeverage):
	name = "tea"

class Chocolate(HotBeverage):
	price = 0.50
	name = "chocolate"
	description = "Chocolate, sweet chocolate..."

class Cappuccino(HotBeverage):
	price = 0.45
	name = "cappuccino"
	description = "Un po' di Italia nella sua tazza!"

def test():
	print(HotBeverage())
	print(Coffee())
	print(Tea())
	print(Chocolate())
	print(Cappuccino())

if __name__ == '__main__':
	test()
