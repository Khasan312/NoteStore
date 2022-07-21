from rest_framework.urls import path
from .views import PurposeView


urlpatterns = [
    path('purpose/', PurposeView.as_view())
]