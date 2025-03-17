from django.shortcuts import render

def markdown_cheatsheet(request):
	return render(request, 'ex00/index.html')
