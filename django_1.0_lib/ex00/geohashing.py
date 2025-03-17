import sys, antigravity

def geohashing():
	if len(sys.argv) != 4:
		return sys.stderr.write("Usage: <latitude> <longitude> <datedow>")
	antigravity.geohash(float(sys.argv[1]), float(sys.argv[2]), sys.argv[3].encode())

if __name__ == '__main__':
	try:
		geohashing()
	except Exception as e:
		print("Error: " + str(e))