from django.urls import path
from rest_framework.decorators import permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.routers import SimpleRouter  # type: ignore
from rest_framework_simplejwt.views import (TokenObtainPairView,
                                            TokenRefreshView)
from users.apps import UsersConfig
from users.views import UserViewSet

app_name = UsersConfig.name

router = SimpleRouter()
router.register(r"users", UserViewSet, basename="users")


urlpatterns = [
    path("login/", TokenObtainPairView.as_view(permission_classes(AllowAny,)), name="token_obtain_pair"),
    path("token/refresh/", TokenRefreshView.as_view(permission_classes(AllowAny,)), name="token_refresh"),
] + router.urls