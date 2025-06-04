from rest_framework.relations import SlugRelatedField
from rest_framework.serializers import ModelSerializer

from sections.models import Section, Content


class ContentSerializer(ModelSerializer):
    """
    Сериализатор контента
    """

    class Meta:
        """
        Настройки параметров сериализатора
        """
        model = Content
        fields = '__all__'


class ContentSectionSerializer(ModelSerializer):
    """
    Сериализатор контента в разделе
    """

    class Meta:
        """
        Настройки параметров сериализатора
        """
        model = Content
        fields = ('id', 'title',)


class ContentListSerializer(ModelSerializer):
    """
    Сериализатор списка контента
    """
    section = SlugRelatedField(slug_field='title', queryset=Section.objects.all())

    class Meta:
        """
        Настройки параметров сериализатора
        """
        model = Content
        fields = ('id', 'section', 'title')
