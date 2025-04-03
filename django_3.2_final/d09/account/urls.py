from django.urls import path
from . import views

urlpatterns = [
	path("", views.display_account, name="account"),
	path("", views.login, name="login"),
	path("", views.logout, name="logout"),
]