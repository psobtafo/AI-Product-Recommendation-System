from django.urls import path
from . import views  # Import views from the same directory

urlpatterns = [
    path('', views.home, name='blog_home'),  # Change 'home' to your actual view name
]

