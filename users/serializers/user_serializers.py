from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from users.models import User
from users.validators import PasswordValidator


class UserSerializer(serializers.ModelSerializer):
    """
    Сериализатор пользователя
    """

    class Meta:
        """
        Настройки параметров сериализатора
        """
        model = User
        fields = ['id', 'email', 'last_name', 'first_name', 'phone', 'is_active']


class UserCreateSerializer(serializers.ModelSerializer):
    """
    Сериализатор создания пользователя
    """
    password = serializers.CharField(write_only=True, required=True, min_length=8, max_length=16)

    class Meta:
        """
        Настройки параметров сериализатора
        """
        model = User
        fields = ['email', 'password']
        validators = [
            PasswordValidator(field='password'),
        ]

    def create(self, validated_data):
        """
        Создание пользователя
        """
        user = User.objects.create(**validated_data)
        user.set_password(user.password)
        user.save()
        return user


class UserUpdateSerializer(serializers.ModelSerializer):
    """
    Сериализатор изменения (обновления) пользователя
    """

    class Meta:
        """
        Настройки параметров сериализатора
        """
        model = User
        fields = ['email', 'last_name', 'first_name', 'password', 'phone', 'is_active']
        # validators = [
    #         PasswordValidator(field='password'),
    #     ]
    #
    # def update(self, instance, validated_data):
    #     password = validated_data.pop('password', None)
    #     instance.set_password(password)
    #     instance.save()
    #     return instance


class UserTokenObtainPairSerializer(TokenObtainPairSerializer):
    """
    Сериализатор получения токена
    """

    @classmethod
    def get_token(cls, user):
        """
        Получение токена
        """
        token = super().get_token(user)
        token['email'] = user.email
        return token
