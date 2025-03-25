from django.shortcuts import render
from django.conf import settings
from django.utils.timezone import now
import random
from django.http import JsonResponse

# Create your views here.
def update_username(request):
	username = request.session.get("username")
	username_timestamp = request.session.get("username_timestamp")

	if not username or not username_timestamp or (now().timestamp() - username_timestamp > settings.SESSION_COOKIE_AGE):
		request.session["username"] = random.choice(settings.USERNAMES)
		request.session["username_timestamp"] = now().timestamp()
		username = request.session["username"]

	if request.headers.get('x-requested-with') == 'XMLHttpRequest':
		return JsonResponse({"username": username})

	context = {
		"username" : username,
	}
	return render(request, "ex/update_username.html", context)