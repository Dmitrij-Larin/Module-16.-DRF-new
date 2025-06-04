from rest_framework.relations import SlugRelatedField
from rest_framework.serializers import ModelSerializer

from sections.models import Question, Section


class QuestionSectionSerializer(ModelSerializer):
    """
    Сериализатор вопросов в разделах
    """
    question_section = SlugRelatedField(slug_field='title', queryset=Section.objects.all())

    class Meta:
        """
        Настройки параметров сериализатора
        """
        model = Question
        fields = ('id', 'question_section')


class QuestionSerializer(ModelSerializer):
    """
    Сериализатор вопросов
    """
    question_section = SlugRelatedField(slug_field='title', queryset=Section.objects.all())

    class Meta:
        """
        Настройки параметров сериализатора
        """
        model = Question
        fields = ('id', 'question_section', 'question')
