from django.shortcuts import render

# Create your views here.
def color_table(request):
	context = {
		"css_file" : "ex03/styles.css",
		"max_iter" : range(50)
	}
	return render(request, "ex03/table.html", context)