from django.shortcuts import render
from django.conf import settings
from django.utils.timezone import now
import random
from django.http import JsonResponse

from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from django.shortcuts import redirect
from .forms import SignUpForm
from .forms import LogInForm

# Create your views here.
def homepage(request):
	if request.user.is_authenticated:
		username = request.user.username
	else:
		username = request.session.get("username")
		username_timestamp = request.session.get("username_timestamp")

		if not username or not username_timestamp or (now().timestamp() - username_timestamp > settings.SESSION_COOKIE_AGE):
			request.session["username"] = random.choice(settings.USERNAMES)
			request.session["username_timestamp"] = now().timestamp()
			username = request.session["username"]

	if request.headers.get('x-requested-with') == 'XMLHttpRequest':
		return JsonResponse({"username": username})

	context = {"username": username}
	return render(request, "ex/homepage.html", context)

def sign_up(request):
	if request.user.is_authenticated:
		return redirect("homepage")
	
	if request.method == "POST":
		form = SignUpForm(request.POST)
		if form.is_valid():
			new_user = form.save(commit=False)
			new_user.set_password(form.cleaned_data["password"])
			new_user.save()

			login(request, new_user)
			return redirect("homepage")
	else:
		form = SignUpForm()

	context = {"form" : form}
	return render(request, "ex/register.html", context)
	
def log_in(request):
	if request.user.is_authenticated:
		return redirect('homepage')

	if request.method == "POST":
		form = LogInForm(request.POST)
		if form.is_valid():
			username = form.cleaned_data["username"]
			password = form.cleaned_data["password"]

			user = authenticate(request, username=username, password=password)
			if user is not None:
				login(request, user)
				return redirect('homepage')
			else:
				form.add_error(None, "Invalid username or password.")
	else:
		form = LogInForm()

	return render(request, "ex/login.html", {"form": form})

def log_out(request):
	logout(request)
	return redirect("homepage")