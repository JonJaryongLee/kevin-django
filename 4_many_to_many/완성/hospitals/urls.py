from django.urls import path
from . import views

app_name = 'hospitals'

urlpatterns = [
    path('', views.index, name='index'),
]