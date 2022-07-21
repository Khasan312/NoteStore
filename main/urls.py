from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import SimpleRouter
from apps.notebook.views import NoteBookWiewSet
from apps.accessories.views import ThingsViewSet
from apps.rewiew.views import ReviewViewSet


#SWAGGER
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi




router = SimpleRouter()

#NOTEBOOK
router.register('notebooks', NoteBookWiewSet)

#THINGS
router.register('things', ThingsViewSet)

#REVIEW
router.register('reviews', ReviewViewSet)



schema_view = get_schema_view(
   openapi.Info(
      title="Bilgisayar",
      default_version='حاسوب',
      description="My API",
    ),
   public=True,
   permission_classes=[permissions.AllowAny],
)



urlpatterns = [
    path('admin/', admin.site.urls),

    #ACCOUNT
    path('api/v1/', include('account.urls')),

    #NOTEBOOK
    path('api/', include(router.urls)),
    path('api/', include('notebook.urls')),

    #CART
    path('api/v1/', include('apps.cart.urls')),

    #HELP
    path('api/v1/', include('help.urls')),

    #ACCESSORIES
    path('api/v1/', include('accessories.urls')),


    path(r'swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path(r'', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path(r'redoc', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),



]
