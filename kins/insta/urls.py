from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("login/", views.user_login, name="login"),
    path("logout/", views.logout1, name="logout"),
    path("dashboard/", views.dashboard, name="dashboard"),
    path("signup/", views.signup, name="signup")
]