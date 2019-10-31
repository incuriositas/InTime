from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('search/<slug:pk>/', views.search, name='search'),
    path('form/', views.form_func, name='form_func'),
]