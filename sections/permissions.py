from django.utils.translation import gettext_lazy as _
from rest_framework.permissions import BasePermission

from users.models import UserRoles


class IsModerator(BasePermission):
    """
    Пользовательское разрешение Модератора
    """
    message = _('You are not a moderator')

    def has_permission(self, request, view):
        """
        Проверка прав доступа
        """
        if request.user.role == UserRoles.MODERATOR:
            return True
        return False


class IsSuperuser(BasePermission):
    """
    Пользовательское разрешение Суперюзера
    """
    message = _('You are not a Superuser')

    def has_permission(self, request, view):
        """
        Проверка прав доступа
        """
        if request.user.is_superuser:
            return True
        return False
