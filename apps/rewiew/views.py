from django.shortcuts import render
from rest_framework import mixins, viewsets
from .serializers import ReviewSerializer

from apps.rewiew.models import Review

class ReviewViewSet(mixins.CreateModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.DestroyModelMixin,
                    viewsets.GenericViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer