from django.urls import path
from .views import IndexView, SalaView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path("chat/<str:room_name>/", SalaView.as_view(), name="room"),
]