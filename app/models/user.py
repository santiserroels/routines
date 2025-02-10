from django.contrib.auth.models import AbstractUser
from django.db.models import EmailField


class User(AbstractUser):
    email = EmailField(max_length=254, unique=True)
