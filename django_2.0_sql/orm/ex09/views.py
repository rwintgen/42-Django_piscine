from django.shortcuts import render
from django.http import HttpResponse
from .models import Planets, People

# Create your views here.
def display_content(request):
	data = People.objects.select_related("homeworld").filter(
		homeworld__climate__icontains="windy"
	).order_by("name")

	if not data:
			return HttpResponse("No data available, please use the following command line before use: python3 manage.py loaddata ex09_initial_data.json")

	context = {
		"css_file": "ex09/styles.css",
		"characters": data
	}
	return render(request, "ex09/display.html", context)