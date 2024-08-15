# Generated by Django 5.0.8 on 2024-08-13 10:18

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Habit",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "place",
                    models.CharField(max_length=100, verbose_name="Место выполнения"),
                ),
                (
                    "time",
                    models.TimeField(
                        verbose_name="Время, когда необходимо выполнить привычку"
                    ),
                ),
                (
                    "action",
                    models.CharField(
                        max_length=100, verbose_name="Действие, которое нужно сделать"
                    ),
                ),
                (
                    "is_pleasant",
                    models.BooleanField(
                        choices=[(True, "Приятная"), (False, "Нет")],
                        default=False,
                        verbose_name="Приятная привычка",
                    ),
                ),
                (
                    "periodicity",
                    models.PositiveIntegerField(
                        default=1, verbose_name="Периодичность выполнения"
                    ),
                ),
                (
                    "reward",
                    models.CharField(
                        blank=True,
                        max_length=100,
                        null=True,
                        verbose_name="Вознаграждение",
                    ),
                ),
                (
                    "execution_time",
                    models.PositiveIntegerField(
                        default=120,
                        help_text="Время в секундах",
                        verbose_name="Время выполнения",
                    ),
                ),
                (
                    "is_public",
                    models.BooleanField(
                        choices=[(True, "Публичная"), (False, "Нет")],
                        default=False,
                        verbose_name="Публичная привычка",
                    ),
                ),
                (
                    "related_habit",
                    models.ForeignKey(
                        blank=True,
                        limit_choices_to={"is_pleasant": True},
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="related_to",
                        to="habits.habit",
                        verbose_name="Связанная привычка",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="habits",
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="Пользователь",
                    ),
                ),
            ],
            options={
                "verbose_name": "Привычка",
                "verbose_name_plural": "Привычки",
            },
        ),
    ]
