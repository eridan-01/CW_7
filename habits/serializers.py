from rest_framework import serializers

from habits.models import Habit
from habits.validators import HabitsValidator, PeriodicityValidator


class HabitSerializer(serializers.ModelSerializer):

    class Meta:
        model = Habit
        fields = "__all__"
        validators = [HabitsValidator, PeriodicityValidator]
