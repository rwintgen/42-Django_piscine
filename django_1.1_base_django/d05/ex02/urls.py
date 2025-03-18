from django.urls import path
from . import views

urlpatterns = [
	path('', views.form_submission, name="form")
]