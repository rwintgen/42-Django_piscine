from django.shortcuts import render

# Create your views here.
def django_history(request):
	context = {
		"css_file" : "ex01/style1.css"
	}
	return(render(request, "ex01/django_history"))

def static_page(request):
	context = {
		"css_file" : "ex01/style1.css"
	}
	return(render(request, "ex01/static_page"))

def templates(request):
	context = {
		"css_file" : "ex01/style2.css"
	}
	return(render(request, "ex01/templates"))