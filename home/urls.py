from django.urls import path

from . import views

urlpatterns = [
    path('home', views.HomveView.as_view(), {}),
    path('authorized', views.AuthorizedView.as_view()),
]