from rest_framework.fields import SerializerMethodField
from rest_framework.serializers import ModelSerializer

from sections.models import Section, Content
from sections.serializers.content_serializers import ContentSectionSerializer


class SectionSerializer(ModelSerializer):
    """
    Сериализатор раздела
    """

    class Meta:
        """
        Настройки параметров сериализатора
        """
        model = Section
        fields = '__all__'


class SectionListSerializer(ModelSerializer):
    """
    Сериализатор списка разделов
    """
    section_content_title = SerializerMethodField()

    def get_section_content_title(self, section):
        """
        Получение названия контента для раздела
        """
        return ContentSectionSerializer(Content.objects.filter(section=section), many=True).data

    class Meta:
        """
        Настройки параметров сериализатора
        """
        model = Section
        fields = ('id', 'title', 'section_content_title')
