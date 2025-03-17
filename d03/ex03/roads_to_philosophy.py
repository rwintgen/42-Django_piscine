import sys
import requests
from bs4 import BeautifulSoup

def fetch_page(url):
	response = requests.get(url)
	response.raise_for_status()
	return BeautifulSoup(response.text, "html.parser")

def get_next_url(soup):
	content = soup.find("div", {"id": "mw-content-text"})

	for link in content.select('p > a'):
		href = link.get("href")
		if href and href.startswith("/wiki/") and not href.startswith("/wiki/Wikipedia:") and not href.startswith("/wiki/Help:"):
			new_link = "https://en.wikipedia.org" + href
			print(new_link)
			return new_link

	return None

def roads_to_philosophy(start):
	url = "https://en.wikipedia.org" + "/wiki/" + start.replace(" ", "_")
	visited = []

	while url is not None:
		soup = fetch_page(url)
		title_tag = soup.find("h1", {"id": "firstHeading"})
		title = title_tag.text if title_tag else "Unknown Title"
		if title in visited:
			print("It leads to an infinite loop!")
			return

		visited.append(title)
		print(title)

		if title == "Philosophy":
			print(f"{len(visited)} roads from {visited[0]} to Philosophy!")
			return

		url = get_next_url(soup)

	print("It leads to a dead end!")

def main():
	if len(sys.argv) != 2:
		print("Usage: python3 roads_to_philosophy.py <starting_page>")
		return

	try:
		roads_to_philosophy(sys.argv[1])
		# roads_to_philosophy("Txorierri line") # infinite loop
	except Exception as e:
		print(f"Error: {e}")
		return

if __name__ == '__main__':
	main()