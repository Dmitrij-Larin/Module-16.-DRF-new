from rest_framework import status
from rest_framework.test import APITestCase

from sections.models import Section, Content, Question
from sections.tests.utils import get_member_user


class ContentTestCase(APITestCase):
    """
    Тестирование вопросов
    """

    def setUp(self):
        """
        Параметры для тестов
        """
        self.user = get_member_user()
        response = self.client.post('/users/token/', {"email": self.user.email, "password": "qwerty"})
        self.access_token = response.json().get("access")
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.access_token}')
        self.test_section = Section.objects.create(
            title="Test Section",
            description="Test Description",
        )
        self.test_content = Content.objects.create(
            section=self.test_section,
            title="Test Title",
            content="Test Content",
        )
        self.test_question = Question.objects.create(
            question_section=self.test_section,
            description='Test Question Description',
            question='Test Question',
            answer='Test Answer',
        )

    def test_13_question_list(self):
        """
        Тест на просмотр списка вопросов
        """
        response = self.client.get('/question/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json()['results'][0]['question_section'], 'Test Section')

    def test_14_question_is_correct(self):
        """
        Тест на правильность ответа на вопрос
        """
        response = self.client.get(f'/question/{self.test_question.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json()['question'], 'Test Question')

        response = self.client.post(f'/question/{self.test_question.id - 1}/', {"user_answer": "Test Answer"})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json().get('is_correct'), True)
