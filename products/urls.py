from django.urls import path
from . import views

urlpatterns =[
    path(' ', views.index),
    path("snippet", views.snippet_details)
]