from django.urls import path
from . import views

urlpatterns = [
	path("init/", views.init_table, name="init"),
	path("populate/", views.populate_table, name="populate"),
	path("display/", views.display_content, name="display"),
	path("remove/", views.remove_row, name="remove")
]