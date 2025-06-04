from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response

from sections.models import Section, Content, Question
from sections.paginators import SectionPaginator, SectionContentPaginator, QuestionPaginator
from sections.permissions import IsModerator
from sections.serializers.content_serializers import ContentSerializer, ContentListSerializer
from sections.serializers.question_serializer import QuestionSerializer
from sections.serializers.section_serializers import SectionListSerializer, SectionSerializer


class SectionListAPIView(ListAPIView):
    """
    Представление списка разделов
    """
    serializer_class = SectionListSerializer
    queryset = Section.objects.all()
    permission_classes = (IsAuthenticated,)
    pagination_class = SectionPaginator


class SectionCreateAPIView(CreateAPIView):
    """
    Представление создания разделов
    """
    serializer_class = SectionSerializer
    permission_classes = (IsAuthenticated, IsAdminUser | IsModerator)


class SectionRetrieveAPIView(RetrieveAPIView):
    """
    Представление информации в разделах
    """
    serializer_class = SectionSerializer
    queryset = Section.objects.all()
    permission_classes = (IsAuthenticated,)


class SectionUpdateAPIView(UpdateAPIView):
    """
    Представление обновления разделов
    """
    serializer_class = SectionSerializer
    queryset = Section.objects.all()
    permission_classes = (IsAuthenticated, IsAdminUser | IsModerator)


class SectionDestroyAPIView(DestroyAPIView):
    """
    Представление удаления разделов
    """
    serializer_class = SectionSerializer
    queryset = Section.objects.all()
    permission_classes = (IsAuthenticated, IsAdminUser | IsModerator)


class ContentListAPIView(ListAPIView):
    """
    Представление списка контента
    """
    serializer_class = ContentListSerializer
    queryset = Content.objects.all()
    permission_classes = (IsAuthenticated,)
    pagination_class = SectionContentPaginator


class ContentCreateAPIView(CreateAPIView):
    """
    Представление создания контента
    """
    serializer_class = ContentSerializer
    permission_classes = (IsAuthenticated, IsAdminUser | IsModerator)


class ContentRetrieveAPIView(RetrieveAPIView):
    """
    Представление информации о контенте
    """
    serializer_class = ContentSerializer
    queryset = Content.objects.all()
    permission_classes = (IsAuthenticated,)


class ContentUpdateAPIView(UpdateAPIView):
    """
    Представление обновления контента
    """
    serializer_class = ContentSerializer
    queryset = Content.objects.all()
    permission_classes = (IsAuthenticated, IsAdminUser | IsModerator)


class ContentDestroyAPIView(DestroyAPIView):
    """
    Представление удаления контента
    """
    serializer_class = ContentSerializer
    queryset = Content.objects.all()
    permission_classes = (IsAuthenticated, IsAdminUser | IsModerator)


class QuestionListAPIView(ListAPIView):
    """
    Представление списка вопросов
    """
    serializer_class = QuestionSerializer
    queryset = Question.objects.all()
    permission_classes = (IsAuthenticated,)
    pagination_class = QuestionPaginator


class QuestionRetrieveAPIView(RetrieveAPIView):
    """
    Представление просмотра вопроса
    """
    serializer_class = QuestionSerializer
    queryset = Question.objects.all()
    permission_classes = (IsAuthenticated,)

    def post(self, request, *args, **kwargs):
        """
        Обработка post запросов
        """
        answers = [question.answer for question in Question.objects.all()]
        answer = answers[self.kwargs.get('pk') - 1].strip().lower()
        user_answer = request.data.get('user_answer').strip().lower()
        is_correct = user_answer == answer
        return Response({'is_correct': is_correct})
