from django.contrib.auth.models import User
from django.contrib.auth import logout 
from .serializers import UserSerializer
from rest_framework import viewsets
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

class CreateUser(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def logout(request):
    logout(request)
    return Response({'message': 'Successfully logged out'})