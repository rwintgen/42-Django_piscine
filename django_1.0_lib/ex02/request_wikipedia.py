import dewiki.parser
import requests, json, dewiki, sys

def create_url(query):
	components = {
		"base": "https://en.wikipedia.org/w/api.php",
		"action": "parse",
		"format": "json",
		"page": query,
		"prop": "wikitext",
		"redirects": "true"
	}

	url = components["base"] + "?"
	url += "&".join([f"{key}={value}" for key, value in components.items() if key != "base"])
	# print(url)
	return url

def main():
	if len(sys.argv) != 2:
		print("Usage: python3 request_wikipedia.py <query>")
		return
	
	try:
		query = sys.argv[1].replace(" ", "_")
		response = requests.get(create_url(query))
		response.raise_for_status()
		data = response.json()
		# with open("raw_data.json", "w") as test:
		# 	test.write(json.dumps(data, indent=4))

		content = data["parse"]["wikitext"]["*"]
		formatted_content = dewiki.from_string(content)
		with open(f"{query}.wiki", "w") as out:
			out.write(formatted_content)

	except Exception as e:
		err_msg = str(e) if data["error"]["info"] is None else data["error"]["info"]
		print("Error: " + err_msg)

if __name__ == '__main__':
	main()