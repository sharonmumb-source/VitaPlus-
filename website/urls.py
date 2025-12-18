from django.urls import path
from . import views

urlpatterns = [
path('', views.home, name='home'),
path('benefits/', views.benefits, name='benefits'),
path('ingredients/', views.ingredients, name='ingredients'),
path('contact/', views.contact, name='contact'),

]
