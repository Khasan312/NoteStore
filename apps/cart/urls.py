from rest_framework.urls import path
from .views import AddItem, OrderView

urlpatterns = [
    path('add-cart/', AddItem.as_view()),
    path('cart/', OrderView.as_view()),
]