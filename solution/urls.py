from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('items/',views.submit.as_view()),
    path('items',views.submit.as_view()),
]
