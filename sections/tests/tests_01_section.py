from rest_framework import status
from rest_framework.test import APITestCase

from sections.models import Section
from sections.tests.utils import get_admin_user, get_member_user


class SectionTestCase(APITestCase):
    """
    Тестирование разделов
    """

    def setUp(self):
        """
        Параметры для тестов
        """
        self.user = get_admin_user()
        response = self.client.post('/users/token/', {"email": self.user.email, "password": "qwerty"})
        self.access_token = response.json().get("access")
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.access_token}')
        self.test_section = Section.objects.create(
            title="Test Section",
            description="Test Description",
        )

    def test_01_section_create(self):
        """
        Тест на создание раздела
        """
        data = {
            "title": "Test Section Create",
            "description": "Test Description Create",
        }
        response = self.client.post('/section/create/', data=data)
        # print(response.status_code)
        # print(response.json())
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.json().get('title'), "Test Section Create")
        self.assertEqual(response.json().get('description'), "Test Description Create")

    def test_02_section_detail(self):
        """
        Тест на просмотр информации раздела
        """
        response = self.client.get(f'/section/{self.test_section.id}/')
        # print(response.json())
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json().get('title'), "Test Section")
        self.assertEqual(response.json().get('description'), "Test Description")

    def test_03_section_update(self):
        """
        Тест на обновление раздела
        """
        data = {
            'title': "Test Section Update Put",
            'description': "Test Section Description Put",
        }
        response = self.client.put(f'/section/{self.test_section.id}/update/', data=data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json().get('title'), "Test Section Update Put")
        self.assertEqual(response.json().get('description'), "Test Section Description Put")

    def test_04_section_delete(self):
        """
        Тест на удаление раздела
        """
        response = self.client.delete(f'/section/{self.test_section.id}/delete/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_05_section_list(self):
        """
        Тест на просмотр списка разделов
        """
        response = self.client.get('/section/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json()['results'][0]['title'], "Test Section")

    def test_06_section_create_forbidden(self):
        """
        Тест на запрет создания пользователем раздела
        """
        self.user = get_member_user()
        response = self.client.post('/users/token/', {"email": self.user.email, "password": "qwerty"})
        self.access_token = response.json().get("access")
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.access_token}')
        data = {
            "title": "Test Section Create",
            "description": "Test Description Create",
        }
        response = self.client.post('/section/create/', data=data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertEqual(response.json().get('detail'), "У вас недостаточно прав для выполнения данного действия.")
