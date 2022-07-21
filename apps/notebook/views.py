from rest_framework.viewsets import ModelViewSet
from apps.notebook.models import NoteBook, Purpose
from rest_framework.generics import ListAPIView
from .serializers import (NoteBookSerializer, PurposeSerializer)
from rest_framework.permissions import IsAuthenticated, AllowAny
from django.db.models import Q




class PurposeView(ListAPIView):
    queryset = Purpose.objects.all()
    serializer_class = PurposeSerializer


class NoteBookWiewSet(ModelViewSet):
    queryset = NoteBook.objects.all()
    serializer_class = NoteBookSerializer
    permission_classes = [IsAuthenticated, ]


    def get_permissions(self):
        if self.action == ['create', 'update', 'destroy']:
            return [IsAuthenticated(),]
        else:
            return [AllowAny(),]

    def get_queryset(self):
        data = super().get_queryset()
        search = self.request.query_params.get('search')
        if search:
            data = data.filter(Q(title__icontains=search))
                            #    Q(balance=search))
        return data

    