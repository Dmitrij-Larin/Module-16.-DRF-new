from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.views import TokenObtainPairView

from users.models import User
from users.serializers.user_serializers import UserSerializer, UserCreateSerializer, UserUpdateSerializer, \
    UserTokenObtainPairSerializer


class UserListAPIView(ListAPIView):
    """
    Представление списка пользователей
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsAuthenticated,)


class UserCreateAPIView(CreateAPIView):
    """
    Преставление создания пользователя
    """
    queryset = User.objects.all()
    serializer_class = UserCreateSerializer
    permission_classes = (IsAuthenticated,)


class UserRetrieveAPIView(RetrieveAPIView):
    """
    Преставление информации о пользователе
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsAuthenticated,)


class UserUpdateAPIView(UpdateAPIView):
    """
    Преставление обновления пользователя
    """
    queryset = User.objects.all()
    serializer_class = UserUpdateSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        """
        Фильтрация пользователей
        """
        user = self.request.user
        return User.objects.filter(id=user.id)


class UserDestroyAPIView(DestroyAPIView):
    """
    Представление удаления пользователя
    """
    queryset = User.objects.all()
    permission_classes = (IsAuthenticated,)


class UserTokenObtainPairView(TokenObtainPairView):
    """
    Представление получения токена пользователем
    """
    serializer_class = UserTokenObtainPairSerializer
