from django.urls import path
from .views import ArticleListView, HomeRedirectView, LoginView, PublicationsListView, ArticleDetailView, LogoutView, FavouritesListView

urlpatterns = [
	path("", HomeRedirectView.as_view(), name="home"),
	path("articles/", ArticleListView.as_view(), name="articles"),
	path("login/", LoginView.as_view(), name="login"),
    path("publications/", PublicationsListView.as_view(), name="publications"),
    path("articles/<int:pk>/", ArticleDetailView.as_view(), name="article_detail"),
	path("logout/", LogoutView.as_view(), name="logout"),
    path("favourites/", FavouritesListView.as_view(), name="favourites"),

]