from django.urls import path
from .views import UserAPIList, UserAPIDetail


urlpatterns = [
    path('users/', UserAPIList.as_view()),
    path('users/<int:pk>', UserAPIDetail.as_view()),
]
