from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _

NULLABLE = {'blank': True, 'null': True}


class UserRoles(models.TextChoices):
    """
    Модель статуса пользователя
    """
    MEMBER = 'member', _('member')
    MODERATOR = 'moderator', _('moderator')


class User(AbstractUser):
    """
    Модель пользователя
    """
    username = None
    email = models.EmailField(unique=True, verbose_name=_('email address'))
    role = models.CharField(max_length=9, choices=UserRoles.choices, default=UserRoles.MEMBER)
    first_name = models.CharField(max_length=50, verbose_name=_('first name'), **NULLABLE)
    last_name = models.CharField(max_length=50, verbose_name=_('last name'), **NULLABLE)
    phone = models.CharField(max_length=20, verbose_name=_('phone number'), **NULLABLE)
    is_active = models.BooleanField(default=True, verbose_name=_('is active'))

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        """
        Представление модели в строковом виде
        """
        return f'{self.email}'

    class Meta:
        """
        Настройка параметров для модели User
        """
        verbose_name = _('user')
        verbose_name_plural = _('users')
        ordering = ['id']
