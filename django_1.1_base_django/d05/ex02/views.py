from django.shortcuts import render

# Create your views here.
def form_submission(request):
	context = {
		"test" : "test"
	}
	return (render(request, "ex02/form.html", context))