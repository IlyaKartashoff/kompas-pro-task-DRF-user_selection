from rest_framework.generics import ListAPIView, RetrieveAPIView

from .serializers import UserSerializer
from .models import User

class UserAPIList(ListAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()

class UserAPIDetail(RetrieveAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()

    