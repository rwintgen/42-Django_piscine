from .models import Article, UserFavouriteArticle
from .forms import RegisterForm
from django.views.generic import ListView, RedirectView, FormView, DetailView
from django.urls import reverse_lazy
from django.shortcuts import redirect
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.views.generic.edit import CreateView

# Create your views here.
class ArticleListView(ListView):
	model = Article
	template_name = "articles.html"
	context_object_name = "articles"

class HomeRedirectView(RedirectView):
	url = reverse_lazy("articles")

class LoginView(FormView):
	template_name = "login.html"
	form_class = AuthenticationForm
	success_url = reverse_lazy("home")

	def form_valid(self, form):
		user = form.get_user()
		login(self.request, user)
		return super().form_valid(form)

	def form_invalid(self, form):
		return self.render_to_response(self.get_context_data(form=form))

class PublicationsListView(LoginRequiredMixin, ListView):
	model = Article
	template_name = "publications.html"
	context_object_name = "articles"

	def get_queryset(self):
		return Article.objects.filter(author=self.request.user)

class ArticleDetailView(DetailView):
	model = Article
	template_name = "article_detail.html"
	context_object_name = "article"

class LogoutView(RedirectView):
	url = reverse_lazy("home")

	def get(self, request, *args, **kwargs):
		logout(request)
		return super().get(request, *args, **kwargs)

class FavouritesListView(LoginRequiredMixin, ListView):
	model = UserFavouriteArticle
	template_name = "favourites.html"
	context_object_name = "favourites"

	def get_queryset(self):
		return UserFavouriteArticle.objects.filter(user=self.request.user)

class RegisterView(CreateView):
	model = User
	template_name = "register.html"
	form_class = RegisterForm
	success_url = reverse_lazy("login")

	def form_valid(self, form):
		new_user = form.save(commit=False)
		new_user.set_password(form.cleaned_data["password"])
		new_user.save()
		login(self.request, new_user)
		return redirect("home")

class PublishView(LoginRequiredMixin, CreateView):
	model = Article
	template_name = "publish.html"
	fields = ["title", "synopsis", "content"]
	success_url = reverse_lazy("publications")

	def form_valid(self, form):
		form.instance.author = self.request.user
		return super().form_valid(form)

class AddToFavouriteView(LoginRequiredMixin, CreateView):
	model = UserFavouriteArticle
	template_name = "add_favourite.html"
	fields = []
	success_url = reverse_lazy("favourites")

	def form_valid(self, form):
		form.instance.user = self.request.user
		form.instance.article = Article.objects.get(pk=self.kwargs["pk"])
		return super().form_valid(form)
