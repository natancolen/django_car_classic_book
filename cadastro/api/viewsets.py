from rest_framework.viewsets import ModelViewSet
from cadastro.models import User
from .serializers import UserSerializers


class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializers
