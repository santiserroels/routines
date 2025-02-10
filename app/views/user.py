from rest_framework.viewsets import ModelViewSet
from app.models import User
from app.serializers import UserSerializer


class UserView(ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()
