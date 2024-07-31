from django.urls import path
from home.views import RegisterAPI


urlpatterns = [
    path('register/', RegisterAPI.as_view())
]
