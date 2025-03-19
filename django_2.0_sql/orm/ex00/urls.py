from django.urls import path
from .views import init_db

urlpatterns = [
    path('init/', init_db, name='init')
]