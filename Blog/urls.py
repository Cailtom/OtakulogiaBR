from django.urls import path
from . import views

app_name = 'otakulogiabr'

urlpatterns = [
    path('', views.otakulogiabr, name='otakulogiabr'),
]
