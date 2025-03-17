import sys
import requests
from bs4 import BeautifulSoup

class WikiScraper:
	BASE_URL = "https://en.wikipedia.org/wiki/"
	GOAL_URL = BASE_URL + "Philosophy"

	def __init__(self, start):
		self.start_url = self.BASE_URL + start.replace(" ", "_")
		self.visited = {start : self.start_url}

	def _get_first_link(self):
		try:
			response = requests.get(self.start_url)
			response.raise_for_status()
		except Exception as e:
			if response.status_code == 404:
				print("It's a dead end!")
			else:
				print("Error: " + str(e))
			return

		soup = BeautifulSoup(response.text, "html.parser")
		# Continue here


if __name__ == '__main__':
	if len(sys.argv) != 2:
		print("Usage: python3 roads_to_philosophy.py <starting pqge>")
		return
	
	try:
		scrap = WikiScraper(sys.argv[1])
		scrap.roads_to_philosophy()
	except Exception as e:
		print("Error: " + str(e))
		return