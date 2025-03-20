from django.urls import path
from . import views

urlpatterns = [
	path("populate/", views.populate_table, name="populate"),
	path("display/", views.display_content, name="display"),
	path("update/", views.update_movie, name="update"),
]