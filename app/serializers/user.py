from rest_framework.serializers import ModelSerializer, EmailField, BooleanField, CharField
from app.models import User


class UserSerializer(ModelSerializer):
    email = EmailField(required=True, allow_blank=False, max_length=256)
    is_active = BooleanField(required=False, default=True)
    first_name = CharField(required=False, allow_blank=True, max_length=256)
    last_name = CharField(required=False, allow_blank=True, max_length=256)

    class Meta:
        model = User
        fields = [
            "id",
            "email",
            "routines"
        ]
