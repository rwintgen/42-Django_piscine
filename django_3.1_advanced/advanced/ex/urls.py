from django.urls import path
from .views import ArticleListView, HomeRedirectView, UserLoginView

urlpatterns = [
	path("", HomeRedirectView.as_view(), name="home"),
	path("articles/", ArticleListView.as_view(), name="articles"),
	path("login/", UserLoginView.as_view(), name="login"),
]