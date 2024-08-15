from rest_framework import serializers


class HabitsValidator:
    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        is_pleasant = value.get("is_pleasant")  # Приятная привычка
        related_habit = value.get("related_habit")  # Связанная привычка
        reward = value.get("reward")  # Вознаграждение
        execution_time = value.get("execution_time")  # Время выполнения

        # Проверка, что приятная привычка не может иметь связанной привычки или вознаграждения
        if is_pleasant:
            if related_habit or reward:
                raise serializers.ValidationError(
                    "У приятной привычки не может быть связанной привычки или вознаграждения."
                )

        # Проверка, что может быть указана только связанная привычка или вознаграждение, но не оба
        if related_habit and reward:
            raise serializers.ValidationError(
                "Может быть указана связанная привычка или вознаграждение, но не оба."
            )

        # Проверка, что время выполнения не превышает 120 секунд
        if execution_time and execution_time > 120:
            raise serializers.ValidationError(
                "Длительность привычки не может быть больше 120 секунд."
            )

        # Проверка, что связанные привычки должны быть приятными привычками
        if related_habit and not related_habit.is_pleasant:
            raise serializers.ValidationError(
                "Связанные привычки должны быть приятными привычками."
            )


class PeriodicityValidator:
    def __init__(self, min_value=1, max_value=7):
        self.min_value = min_value
        self.max_value = max_value

    def __call__(self, value):
        if value < self.min_value or value > self.max_value:
            raise serializers.ValidationError(
                f"Периодичность выполнения должна быть от {self.min_value} до {self.max_value} дней."
            )
