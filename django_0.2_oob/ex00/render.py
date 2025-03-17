import sys
import settings

def open_and_read():
	if (len(sys.argv) != 2 or not sys.argv[1].endswith(".template")):
		print("Usage: python3 render.py <file_name>.template")
		return
	
	try:
		vars = {key: value for key, value in settings.__dict__.items()}

		with open(sys.argv[1], "r") as template_file:
			new_file = sys.argv[1].split(".")[0] + ".html"
			with open(new_file, "w") as out:
				templ_content = template_file.read()
				exp_content = templ_content.format(**vars)
				out.write(exp_content)

	except Exception as e:
		print("Error: ", e)

open_and_read()