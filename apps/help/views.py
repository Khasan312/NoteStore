from rest_framework.generics import ListAPIView, CreateAPIView
from .serializers import HelpSerializer, AboutUsSerializer
from apps.help.models import Help, AboutUs
from rest_framework.permissions import IsAdminUser

class HelpView(ListAPIView):
    queryset = Help.objects.all()
    serializer_class = HelpSerializer


class HelpCreate(CreateAPIView):
    queryset = Help.objects.all()
    serializer_class = HelpSerializer
    permission_classes = [IsAdminUser, ]



class AboutUsView(ListAPIView):
    queryset = AboutUs.objects.all()
    serializer_class = AboutUsSerializer