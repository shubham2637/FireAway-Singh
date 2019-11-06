from django.urls import path,include
from . import views
from django.contrib.auth.views import LoginView,LogoutView
urlpatterns =[
    path("", views.index, name="index"),
    path("accounts/", include('django.contrib.auth.urls')),
    ]
