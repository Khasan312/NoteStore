from http.client import ImproperConnectionState
from django.shortcuts import get_object_or_404, render
from rest_framework.views import APIView
from rest_framework.generics import ListCreateAPIView
from django.contrib.auth import get_user_model
from rest_framework.response import Response
from rest_framework import status
from .serializers import RegisterSerializer, UserSerializer, LoginSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.authtoken.models import Token


User = get_user_model()

class UserApiView(ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class RegistrationView(APIView):
    def post(self, request):
        data = request.data
        serializer = RegisterSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            message = '''
                    you have successfully registered!!
                    a registration email has been sent to you
                        '''
            return Response(message, status=status.HTTP_201_CREATED)


class ActivationView(APIView):
    def get(self, request, activation_code):
        user = get_object_or_404(User, activation_code=activation_code)
        user.is_active = True
        user.activation_code = ''
        user.save()
        return Response('Your account successfully activated', status=status.HTTP_200_OK)



class LoginView(TokenObtainPairView):
    serializer_class = LoginSerializer


class LogoutView(APIView):
    permission_classes = [IsAuthenticated, ]

    def post(self, request):
        try:
            request.user.auth_token.delete()
        except AttributeError:
            pass
        from django.contrib.auth import logout

        logout(request)

        return Response('successfully logout', status=status.HTTP_200_OK)