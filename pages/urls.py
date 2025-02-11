from django.urls import path
from .views import HomeView, AboutUsView
urlpatterns = [
    path(route='', view=HomeView.as_view(), name='home'),
    path(route='aboutus/', view=AboutUsView.as_view(), name='aboutus')
]
