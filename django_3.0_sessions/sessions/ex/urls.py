from django.urls import path
from .views import update_username

urlpatterns = [
	path("", update_username, name="update_username")
]