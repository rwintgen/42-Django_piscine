from django.urls import path
from . import views

urlpatterns = [
	path('django/', views.django_history, name='django_history'),
	path('static/', views.static_page, name='static_page'),
	path('templates/', views.templates, name='templates'),
]