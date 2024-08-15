from celery import shared_task

from habits.models import Habit

from habits.services import send_telegram_message


@shared_task
def send_habit():
    habits = Habit.objects.filter(is_pleasant=False)

    for habit in habits:
        tg_chat_id = habit.user.tg_chat_id
        print(habit.action)
        if tg_chat_id:  # Проверяем, что tg_chat_id не пустой
            message = f"Напоминание: Сегодня я должен {habit.action}, в {habit.time}. Место: {habit.place}."
            send_telegram_message(tg_chat_id, message)
        else:
            print(f"Пользователь {habit.user.first_name} {habit.user.last_name} не указал Telegram ID.")
