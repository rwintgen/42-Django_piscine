from django.views.generic import ListView, RedirectView, FormView
from .models import Article
from django.urls import reverse_lazy
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login

# Create your views here.
class ArticleListView(ListView):
	model = Article
	template_name = "articles.html"
	context_object_name = "articles"

class HomeRedirectView(RedirectView):
	url = reverse_lazy("articles")

class UserLoginView(LoginView):
	template_name = "login.html"
	success_url = reverse_lazy("home")