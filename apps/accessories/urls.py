from rest_framework.urls import path

from .views import  ThingsView


urlpatterns = [
    path('things/', ThingsView.as_view()),
    path('things-list/', ThingsView.as_view())
    
]