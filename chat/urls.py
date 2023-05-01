from django.urls import path
from .views import IndexView, SalaView
from django.contrib.auth import views

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path("chat/<str:room_name>/", SalaView.as_view(), name="room"),
    path("login/", views.LoginView.as_view(template_name="login.html"), name="login"),
    path("logout/", views.LogoutView.as_view(), name="logout"),
]