from rest_framework.urls import path
from .views import ActivationView, LoginView, LogoutView, RegistrationView, UserApiView


urlpatterns = [
    path('all-users', UserApiView.as_view()),
    path('register/', RegistrationView.as_view()),
    path('activate/<str:activation_code>/', ActivationView.as_view()),
    path('login/', LoginView.as_view()),
    path('logout/', LogoutView.as_view()),
]   