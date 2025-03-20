from django.urls import path
from .views import init_table

urlpatterns = [
    path('init/', init_table, name='init')
]