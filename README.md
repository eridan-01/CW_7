# __Контекст__

В 2018 году Джеймс Клир написал книгу «Атомные привычки», которая посвящена приобретению новых полезных привычек и искоренению старых плохих привычек. 
Заказчик прочитал книгу,впечатлился и обратился к вам с запросом реализовать трекер полезных привычек.

## __В рамках учебного проекта надо реализовать бэкенд-часть SPA веб-приложения.__

### ___Описание задач___

1. Добавьте необходимые модели привычек.
2. Реализуйте эндпоинты для работы с фронтендом.
3. Создайте приложение для работы с Telegram и рассылками напоминаний.

### ___Модели___
В книге хороший пример привычки описывается как конкретное действие, которое можно уложить в одно предложение:

### __Я буду [ДЕЙСТВИЕ] в [ВРЕМЯ] в [МЕСТО]__

За каждую полезную привычку необходимо себя вознаграждать или сразу после делать приятную привычку. 
Но при этом привычка не должна расходовать на выполнение больше двух минут.

Чем отличается полезная привычка от приятной и связанной?
Полезная привычка — это само действие, которое пользователь будет совершать и получать за его выполнение 
определенное вознаграждение (приятная привычка или любое другое вознаграждение).

Приятная привычка — это способ вознаградить себя за выполнение полезной привычки.

### ___Настройки___

* Исключить одновременный выбор связанной привычки и указания вознаграждения.

* Время выполнения должно быть не больше 120 секунд.

* В связанные привычки могут попадать только привычки с признаком приятной привычки.

* У приятной привычки не может быть вознаграждения или связанной привычки.

* Нельзя выполнять привычку реже, чем 1 раз в 7 дней.

* Для вывода списка привычек реализовать пагинацию с выводом по 5 привычек на страницу.

* Каждый пользователь имеет доступ только к своим привычкам по механизму CRUD.

* Пользователь может видеть список публичных привычек без возможности их как-то редактировать или удалять.

* Интегрировать сервис с мессенджером Телеграм, который будет заниматься рассылкой уведомлений.

* Для проекта необходимо настроить CORS, чтобы фронтенд мог подключаться к проекту на развернутом сервере.

* Для реализации экранов силами фронтенд-разработчиков необходимо настроить вывод документации.
