from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.http import JsonResponse

# Create your views here.
def display_account(request):
	if request.user.is_authenticated:
		context = {"user": request.user}
	else:
		context = {"form": AuthenticationForm()}
	return render(request, "account/account.html", context)

def login_view(request):
	if request.method == "POST":
		form = AuthenticationForm(data=request.POST)
		if form.is_valid():
			user = form.get_user()
			login(request, user)
			return JsonResponse({"success": True, "user": user.username})
		else:
			return JsonResponse({"success": False, "errors": form.errors})
	return JsonResponse({"success": False, "errors": "Invalid request method"})

def logout_view(request):
	if request.method == "POST":
		logout(request)
		return JsonResponse({"success": True})
	return JsonResponse({"success": False, "errors": "Invalid request method"})