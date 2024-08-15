from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from users.models import User
from .models import Habit


class HabitTestCase(APITestCase):
    def setUp(self):
        # Создание пользователя
        self.user = User.objects.create(email="testuser@example.com", password="123qwe")

        # Создание привычки
        self.habit = Habit.objects.create(
            user=self.user,
            place="Дом",
            time="18:00:00",
            action="Выбросить мусор",
            is_pleasant=False,
            periodicity=1,
            execution_time=120,
            is_public=True
        )

        # Аутентификация клиента
        self.client.force_authenticate(user=self.user)

    def test_create_habit(self):
        """ Тест на создание привычки """
        url = reverse("habits:habits_create")
        data = {
                "user": self.user.pk,
                "place": "Дом",
                "time": "18:00:00",
                "action": "Выбросить мусор",
                "is_pleasant": False,
                "periodicity": 1,
                "execution_time": 120,
                "is_public": True
            }
        response = self.client.post(url, data, format="json")

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(data.get("user"), self.user.pk)
        self.assertEqual(data.get("place"), "Дом")
        self.assertEqual(data.get("time"), "18:00:00")
        self.assertEqual(data.get("action"), "Выбросить мусор")
        self.assertEqual(data.get("is_pleasant"), False)
        self.assertEqual(data.get("periodicity"), 1)
        self.assertEqual(data.get("execution_time"), 120)
        self.assertEqual(data.get("is_public"), True)

    def test_list_habit(self):
        """ Тест на просмотр привычки """
        url = reverse("habits:habits_list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data["results"]), 1)
        self.assertEqual(response.data["results"][0]["place"], "Дом")

    def test_retrieve_lesson(self):
        """ Тест на получение привычки """
        url = reverse("habits:habits_retrieve", args=(self.habit.pk,))
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["place"], "Дом")
        self.assertEqual(response.data["time"], "18:00:00")
        self.assertEqual(response.data["action"], "Выбросить мусор")
        self.assertEqual(response.data["is_pleasant"], False)
        self.assertEqual(response.data["periodicity"], 1)
        self.assertEqual(response.data["execution_time"], 120)
        self.assertEqual(response.data["is_public"], True)

    def test_update_habit(self):
        """ Тест на изменение привычки """
        url = reverse("habits:habits_update", args=(self.habit.pk,))
        data = {
            "user": self.user.pk,
            "place": "Дом",
            "time": "18:00:00",
            "action": "Помыть посуду",
            "is_pleasant": False,
            "periodicity": 1,
            "execution_time": 120,
            "is_public": True
        }
        response = self.client.put(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.habit.refresh_from_db()
        self.assertEqual(self.habit.action, "Помыть посуду")

    def test_delete_habit(self):
        """ Тест на удаление привычки """
        url = reverse("habits:habits_delete", args=(self.habit.pk,))
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Habit.objects.count(), 0)

    def test_list_public_habit(self):
        """ Тест вывода публичных привычек """

        response = self.client.get(reverse('habits:public_habits_list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
