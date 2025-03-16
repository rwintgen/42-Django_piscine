import requests, json, dewiki, sys

def main():
	if len(sys.argv) != 2:
		print("Usage: python3 request_wikipedia.py <query>")
		return
	
	query = sys.argv[1].replace(" ", "_")
	response = requests.get(create_url(query))
	# if repsonse not successful error
	# get content from wiki page
	# format content dewiki
	# create file .wiki and write content
	


if __name__ == '__init__':
	main()