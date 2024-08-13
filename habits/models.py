from django.db import models
from django.conf import settings

NULLABLE = {'blank': True, 'null': True}


class Habit(models.Model):
    IS_GOOD_CHOICES = (
        (True, 'Приятная'),
        (False, 'Нет'),
    )

    PUBLIC_CHOICES = (
        (True, 'Публичная'),
        (False, 'Нет'),
    )

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='habits',
        verbose_name='Пользователь'
    )

    place = models.CharField(
        max_length=100,
        verbose_name='Место выполнения'
    )

    time = models.TimeField(
        verbose_name='Время, когда необходимо выполнить привычку'
    )

    action = models.CharField(
        max_length=100,
        verbose_name='Действие, которое нужно сделать'
    )

    is_pleasant = models.BooleanField(
        default=False,
        choices=IS_GOOD_CHOICES,
        verbose_name='Приятная привычка'
    )

    related_habit = models.ForeignKey(
        'self',
        on_delete=models.SET_NULL,
        related_name='related_to',
        limit_choices_to={'is_pleasant': True},
        verbose_name='Связанная привычка',
        **NULLABLE
    )

    periodicity = models.PositiveIntegerField(
        default=1,
        verbose_name='Периодичность выполнения'
    )

    reward = models.CharField(
        max_length=100,
        verbose_name='Вознаграждение',
        **NULLABLE
    )

    execution_time = models.PositiveIntegerField(
        help_text="Время в секундах",
        default=120,
        verbose_name='Время выполнения'
    )

    is_public = models.BooleanField(
        default=False,
        choices=PUBLIC_CHOICES,
        verbose_name='Публичная привычка'
    )

    class Meta:
        verbose_name = 'Привычка'
        verbose_name_plural = 'Привычки'

    def __str__(self):
        return f"{self.action} в {self.time} в {self.place}"
