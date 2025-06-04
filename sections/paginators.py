from rest_framework.pagination import PageNumberPagination


class SectionPaginator(PageNumberPagination):
    """
    Пагинация разделов
    """
    page_size = 3
    page_query_param = 'page_size'
    max_page_size = 10


class SectionContentPaginator(SectionPaginator):
    """
    Пагинация контента
    """
    page_size = 10


class QuestionPaginator(SectionPaginator):
    """
    Пагинация вопросов
    """
    page_size = 5
