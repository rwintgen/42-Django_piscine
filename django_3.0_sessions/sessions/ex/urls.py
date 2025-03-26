from django.urls import path
from .views import homepage, sign_up, log_in, log_out

urlpatterns = [
	path("", homepage, name="homepage"),
	path("register/", sign_up, name="register"),
	path("login/", log_in, name="login"),
	path("logout/", log_out, name="logout"),
]