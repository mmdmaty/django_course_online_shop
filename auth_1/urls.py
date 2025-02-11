from django.urls import path
from .views import signup
urlpatterns = [
    path(route='signup/',view=signup.as_view(),name='signup')
]