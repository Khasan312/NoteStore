from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import ListAPIView
from apps.accessories.models import Bag
from .serializers import ThingSerializer
from rest_framework.permissions import IsAdminUser, AllowAny


class ThingsView(ListAPIView):
    queryset = Bag.objects.all()
    serializer_class = ThingSerializer
    permission_classes = [AllowAny, ]

class ThingsViewSet(ModelViewSet):
    queryset = Bag.objects.all()
    serializer_class = ThingSerializer
    permission_classes = [IsAdminUser, ]

    def get_permissions(self):
        if self.action == ['retrieve', 'create', 'update']:
            return [IsAdminUser(),]
        else:
            return [AllowAny(),]
