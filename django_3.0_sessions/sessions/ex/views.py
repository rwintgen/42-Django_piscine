import random
from django.shortcuts import render
from django.conf import settings
from django.utils.timezone import now
from django.http import JsonResponse
from django.contrib.auth import login, authenticate, logout
from django.shortcuts import redirect
from .forms import SignUpForm, LogInForm, PostTipForm
from .models import Tip
from django.shortcuts import get_object_or_404

# Create your views here.
def handle_creation(request):
	form = PostTipForm(request.POST)
	if form.is_valid():
		tip = form.save(commit=False)
		tip.author = request.user
		tip.save()

def handle_upvote(request, tip_id):
	tip = get_object_or_404(Tip, id=tip_id)
	if request.user in tip.downvotes.all():
		tip.downvotes.remove(request.user)
	if request.user in tip.upvotes.all():
		tip.upvotes.remove(request.user)
	else:
		tip.upvotes.add(request.user)

def handle_downvote(request, tip_id):
	tip = get_object_or_404(Tip, id=tip_id)
	if tip.author == request.user or request.user.has_perm("ex.can_downvote_tip"):
		if request.user in tip.upvotes.all():
			tip.upvotes.remove(request.user)
		if request.user in tip.downvotes.all():
			tip.downvotes.remove(request.user)
		else:
			tip.downvotes.add(request.user)

def handle_delete(request, tip_id):
	tip = get_object_or_404(Tip, id=tip_id)
	if tip.author == request.user or request.user.has_perm("delete_tip"):
		tip.delete()

def homepage(request):
	if request.user.is_authenticated:
		username = request.user.username
		has_delete_perm = request.user.has_perm("ex.delete_tip")
		has_downvote_perm = request.user.has_perm("ex.can_downvote_tip")

		if request.method == "POST":
			if "create_tip" in request.POST:
				handle_creation(request)
			elif "upvote" in request.POST:
				handle_upvote(request, request.POST.get("tip_id"))
			elif "downvote" in request.POST:
				handle_downvote(request, request.POST.get("tip_id"))
			elif "delete" in request.POST:
				to_del = handle_delete(request, request.POST.get("tip_id"))
			return redirect("homepage")
		else:
			form = PostTipForm()
	else:
		username = request.session.get("username")
		username_timestamp = request.session.get("username_timestamp")

		if not username or not username_timestamp or (now().timestamp() - username_timestamp > settings.SESSION_COOKIE_AGE):
			request.session["username"] = random.choice(settings.USERNAMES)
			request.session["username_timestamp"] = now().timestamp()
			username = request.session["username"]

		form = None
		has_delete_perm = False
		has_downvote_perm = False
	
	tips = Tip.objects.all().order_by("-date")

	if request.headers.get('x-requested-with') == 'XMLHttpRequest':
		return JsonResponse({"username": username})

	context = {
		"username": username,
		"form": form,
		"tips": tips,
		"has_delete_perm" : has_delete_perm,
		"has_downvote_perm" : has_downvote_perm
	}
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

	context = {"form" : form}
	return render(request, "ex/login.html", context)

def log_out(request):
	logout(request)
	return redirect("homepage")