from django.urls import path

from . import views

app_name = 'ethparserapp'

urlpatterns = [
    path('', views.main, name='main')
]