from rest_framework.urls import path
from .views import AboutUsView, HelpCreate, HelpView


urlpatterns = [
    #HELP
    path('help/', HelpView.as_view()),
    
    #ADMIN PERMISSION
    path('create-help/', HelpCreate.as_view()),

    #ABOUT US
    path('about-us/', AboutUsView.as_view()),
]