from django.contrib import admin
from django.urls import path
from rest_framework_simplejwt import views as jwt_views
from app.views import UserView

BASE_API_PATH = 'api/v1/'

urlpatterns = [
    path('admin/', admin.site.urls),
    path(BASE_API_PATH + 'token/', jwt_views.TokenObtainPairView.as_view()),
    path(BASE_API_PATH + 'token/refresh/', jwt_views.TokenRefreshView.as_view()),
    path(BASE_API_PATH + 'token/refresh/', UserView.as_view({"post": "create", "get": "retrieve", "delete": "destroy", "put": "update"})),
]
