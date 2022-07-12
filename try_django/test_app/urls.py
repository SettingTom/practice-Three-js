from django.urls import path 
from . import views

app_name = 'test_app'
urlpatterns = [
    path(r'', views.index, name='index'),
]