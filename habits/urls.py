from django.urls import path


from habits.apps import HabitsConfig
from habits.views import (
    HabitListAPIView,
    HabitCreateAPIView,
    HabitUpdateAPIView,
    HabitRetrieveAPIView,
    HabitDestroyAPIView,
    HabitPublicListAPIView,
)

app_name = HabitsConfig.name


urlpatterns = [
    path("habits/", HabitListAPIView.as_view(), name="habits_list"),
    path("habits/<int:pk>/", HabitRetrieveAPIView.as_view(), name="habits_retrieve"),
    path("habits/create/", HabitCreateAPIView.as_view(), name="habits_create"),
    path("habits/<int:pk>/update/", HabitUpdateAPIView.as_view(), name="habits_update"),
    path(
        "habits/<int:pk>/delete/", HabitDestroyAPIView.as_view(), name="habits_delete"
    ),
    path("public_habits/", HabitPublicListAPIView.as_view(), name="public_habits_list"),
]
