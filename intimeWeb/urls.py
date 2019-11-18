from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('#', views.form_func, name='form_func'),
]