# api_final

## Автор:
Эдуард" [Bem6u](https://github.com/Bem6u) Насыров


## Описание:
api final - это REST API для блог-платформы Yatube. Позволяет просматривать и отправлять посты, просматривать группы, подписываться на авторов.

## Как запустить проект:

Клонировать репозиторий и перейти в него в командной строке:

```
git clone https://github.com/bem6u/api_final_yatube.git
```

```
cd api_final_yatube
```

Cоздать и активировать виртуальное окружение:

```
python -m venv env
```

```
для Mac - source env/bin/activate
для Windows source env/Scripts/activate 
```

Установить зависимости из файла requirements.txt:

```
python -m pip install --upgrade pip
```

```
pip install -r requirements.txt
```

Выполнить миграции:

```
python manage.py migrate
```

Запустить проект:

```
python manage.py runserver
```
## Примеры запросов:
### Запрос JWT токена с использованием логина и пароля пользователя SneakyFox:
```
  [POST].../api/v1/jwt/create/
  {
    "username": "ExampleUser",
    "password": "123456780"
}
```
### Ответ:
```
{"refresh": "tyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ0.tyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTY1MjA5NTYwNywianRpIjoiMDBmMGI0MG.sE5Bd3vrnQLIAL5GxxFg36tPoYyB9I5MQBE_iGshpK4",
    "access": "tyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.tyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjUyMDk1NjA3LCJqdGkiOiI0YmIxN2MzODcwNGU0YzQ0OWQ4Nzg4NzA4ODcyZTliMCIsInVzZXJfaWQiOjF9"
}
```
### Запрос с использованием токена пользователя ExampleUser для публикации поста:
```
    [POST].../api/v1/posts/
    {
    "text": "Бэмби — главный персонаж мультфильма. Впервые мы видим его совсем маленьким, едва умеющим ходить. Он робок и пуглив, но быстро привыкает ко всему новому и учится радоваться жизни.",
    "group": 1   
    }
```

### Ответ:
```
{
    "id": 2,
    "text": "Бэмби (Bambi): Бэмби — главный персонаж мультфильма. Впервые мы видим его совсем маленьким, едва умеющим ходить. Он робок и пуглив, но быстро привыкает ко всему новому и учится радоваться жизни.",
    "author": "ExampleUser",
    "image": null,
    "group": 1,
    "pub_date": "2023-03-08T11:48:48.782688Z"
}
```
### Запрос для просмотра групп анонимным пользователем:
```
    [GET].../api/v1/groups/
```
### Пример ответа:
```
    [
    {
        "id": 1,
        "title": "Клуб любителей оленей",
        "slug": "deerlovers",
        "description": "бла-бла-бла"
    },
    {
        "id": 2,
        "title": "Котолюбители",
        "slug": "catslovers",
        "description": "Мур ^^"
    }
]
```

### Подробная документация в формате ReDoc доступна по адресу .../redoc/