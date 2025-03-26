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