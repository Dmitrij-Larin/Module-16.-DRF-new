import re

from django.core.exceptions import ValidationError


class PasswordValidator:
    """
    Валидатор пароля
    """

    def __init__(self, field):
        """
        Инициализация поля проверки
        """
        self.field = field

    def __call__(self, value):
        """
        Проверка логики валидации
        """
        reg_pattern = re.compile(r'^[a-zA-Z0-9]+$')
        tmp_value = dict(value).get(self.field)
        if not bool(reg_pattern.match(tmp_value)):
            raise ValidationError("Пароль должен содержать только латинские буквы и цифры")
