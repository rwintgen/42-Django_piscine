from django.shortcuts import render
from django.http import HttpResponse
from .forms import Ex10Form
from .models import People

# Create your views here.
def character_lookup(request):
	result = []
	query_failed = False

	if request.method == "POST":
		form = Ex10Form(request.POST)
		if form.is_valid():
			min_date = form.cleaned_data["min_date"]
			max_date = form.cleaned_data["max_date"]
			min_diameter = form.cleaned_data["min_diameter"]
			gender = form.cleaned_data["gender"]

			result = People.objects.filter(
				gender=gender,
				homeworld__diameter__gte=min_diameter,
				movies__release_date__range=(min_date, max_date)
			).select_related("homeworld").prefetch_related("movies").distinct()

		if not result:
			query_failed = True
	else:	
		form = Ex10Form()
		if not form.fields["gender"].choices:
			return HttpResponse("No data available, please use the following command line before use: python3 manage.py loaddata ex10_initial_data.json")

	print(result)
	context = {
		"form" : form,
		"result" : result,
		"query_failed" : query_failed,
		"css_file" : "ex10/styles.css"
	}
	return render(request, "ex10/search.html", context)