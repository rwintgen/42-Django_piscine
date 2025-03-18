from django.shortcuts import render
from django.conf import settings
from django.utils import timezone
from .forms import Ex02Form
import os

# Create your views here.

def form_submission(request):
	log_file = settings.FORM_LOG_FILE
	history = []

	if request.method == "POST":
		form = Ex02Form(request.POST)
		if form.is_valid():
			input = form.cleaned_data["text_input"]
			time = timezone.now().strftime("%Y-%m-%d %H:%M:%S")
			log = time + " - " + input + "\n"

			with open(log_file, 'a') as logs:
				logs.write(log)
	form = Ex02Form()

	if os.path.exists(log_file):
		with open(log_file, "r") as logs:
			for line in logs:
				history.append(line.strip())

	context = {
		"form" : form,
		"history" : history
	}
	return (render(request, "ex02/form.html", context))