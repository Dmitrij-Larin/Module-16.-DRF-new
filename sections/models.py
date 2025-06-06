from django.db import models
from django.utils.translation import gettext_lazy as _

from users.models import NULLABLE


class Section(models.Model):
    """
    Модель раздела
    """
    title = models.CharField(max_length=150, verbose_name=_('title'))
    description = models.TextField(verbose_name=_('Discription'), **NULLABLE)

    def __str__(self):
        """
        Представление модели в строковом виде
        """
        return f'{self.title}'

    class Meta:
        """
        Настройки параметров модели Section
        """
        verbose_name = _('Section')
        verbose_name_plural = _('Sections')
        ordering = ['id']


class Content(models.Model):
    """
    Модель контента
    """
    section = models.ForeignKey(Section, on_delete=models.CASCADE, verbose_name=_('Section'))
    title = models.CharField(max_length=150, verbose_name=_('Title'))
    content = models.TextField(verbose_name=_('Content'))

    def __str__(self):
        """
        Представление модели в строковом виде
        """
        return f'{self.title}'

    class Meta:
        """
        Настройки параметров модели Content
        """
        verbose_name = _('Content')
        verbose_name_plural = _('Contents')
        ordering = ['id']


class Question(models.Model):
    """
    Модель вопроса
    """
    question_section = models.ForeignKey(Section, on_delete=models.CASCADE, verbose_name=_('Section'))
    description = models.TextField(verbose_name=_('Description'), **NULLABLE)
    question = models.TextField(verbose_name=_('Question'), **NULLABLE)
    answer = models.CharField(max_length=40, verbose_name=_('Answer'), **NULLABLE)

    def __str__(self):
        """
        Представление модели в строковом виде
        """
        return f'Вопрос по курсу {self.question_section.title}'

    class Meta:
        """
        Настройки параметров модели Content
        """
        verbose_name = _('Question')
        verbose_name_plural = _('Questions')
        ordering = ['question_section']
