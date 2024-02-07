## Установка и запуск:

- У пользователя должны быть установлены [Docker]([url](https://docs.docker.com/engine/install/)) и [Docker Compose]([url](https://docs.docker.com/compose/install/)).
- Склонировать репозиторий из github:

`git clone https://github.com/MisterFlicker/the_menu.git`

- Из директории the_menu выполнить:

`docker-compose build`

`docker-compose up`

По адресу http://0.0.0.0:8000/ будет доступна заглавная страница проекта.

## О проекте:

Проект представляет собой реализацию древовидного меню с помощью Django (template tags) без применения сторонних библиотек.
Само меню хранится в PostgreSQL.
Выбранный пункт меню идентифицируется, благодаря URL страницы.
Для отображения меню используется 1 запрос к базе данных.