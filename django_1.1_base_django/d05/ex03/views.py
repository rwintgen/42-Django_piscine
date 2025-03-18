from django.shortcuts import render

# Create your views here.
def generate_shades(rgb, iter):
	shades = []
	for i in range(iter):
		shade = [
			int(rgb[0] * (1 - i / (iter - 1))),
			int(rgb[1] * (1 - i / (iter - 1))),
			int(rgb[2] * (1 - i / (iter - 1)))
		]
		shades.append(f"rgb({shade[0]}, {shade[1]}, {shade[2]})")
	return shades


def color_table(request):
	lines_nb = 50
	all_shades = {}
	starting_colors = {
		"noir" : [255, 255, 255],
		"rouge" : [255, 0, 0],
		"bleu" : [0, 0, 255],
		"vert" : [0, 255, 0], 
	}

	for color, rgb in starting_colors.items():
		all_shades[color] = generate_shades(rgb, lines_nb)

	# print("All shades dictionary:")
	# for color, shades in all_shades.items():
	# 	print(f"{color}: {shades}")

	context = {
		"css_file" : "ex03/styles.css",
		"colors" : all_shades,
		"max_iter" : range(lines_nb)
	}
	return render(request, "ex03/table.html", context)