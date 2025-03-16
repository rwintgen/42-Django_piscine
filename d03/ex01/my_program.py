from local_lib.path import Path

def test():
	folder = Path("random_folder")
	file = folder / "random_file"

	if not folder.exists():
		folder.mkdir()

	file.write_text("something")
	print(file.read_text())


if __name__ == "__main__":
	test()