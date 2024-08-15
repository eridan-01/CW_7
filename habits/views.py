from rest_framework.generics import (
    CreateAPIView,
    ListAPIView,
    RetrieveAPIView,
    UpdateAPIView,
    DestroyAPIView,
)
from rest_framework.permissions import IsAuthenticated, AllowAny

from habits.models import Habit
from habits.paginators import CustomPagination
from habits.serializers import HabitSerializer
from users.permissions import IsOwner


class HabitCreateAPIView(CreateAPIView):
    serializer_class = HabitSerializer
    permission_classes = (IsAuthenticated,)

    def perform_create(self, serializer):
        habit = serializer.save()
        habit.user = self.request.user
        habit.save()


class HabitListAPIView(ListAPIView):
    serializer_class = HabitSerializer
    queryset = Habit.objects.all()
    pagination_class = CustomPagination
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        queryset = self.queryset.filter(user=self.request.user)
        return queryset


class HabitRetrieveAPIView(RetrieveAPIView):
    serializer_class = HabitSerializer
    queryset = Habit.objects.all()
    permission_classes = (IsAuthenticated, IsOwner)


class HabitUpdateAPIView(UpdateAPIView):
    serializer_class = HabitSerializer
    queryset = Habit.objects.all()
    permission_classes = (IsAuthenticated, IsOwner)


class HabitDestroyAPIView(DestroyAPIView):
    queryset = Habit.objects.all()
    permission_classes = (IsAuthenticated, IsOwner)


class HabitPublicListAPIView(ListAPIView):
    serializer_class = HabitSerializer
    queryset = Habit.objects.filter(is_public=True)
    permission_classes = (AllowAny,)
    pagination_class = CustomPagination
