from django.urls import path
from .views import ArticleListView, HomeRedirectView, LoginView

urlpatterns = [
	path("", HomeRedirectView.as_view(), name="home"),
	path("articles/", ArticleListView.as_view(), name="articles"),
	path("login/", LoginView.as_view(), name="login"),
]