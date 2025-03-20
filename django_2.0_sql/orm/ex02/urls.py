from django.urls import path
from . import views

urlpatterns = [
    path("init/", views.init_db, name="init"),
    path("populate/", views.populate_table, name="populate"),
    path("display/", views.display_content, name="display")
]