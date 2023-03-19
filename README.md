# api_final

## Используемые технологии:
asgiref==3.6.0
attrs==22.2.0
certifi==2022.12.7
cffi==1.15.1
charset-normalizer==2.0.12
coreapi==2.3.3
coreschema==0.0.4
cryptography==39.0.2
defusedxml==0.7.1
Django==3.2.16
django-filter==1.1.0
django-templated-mail==1.1.1
djangorestframework==3.12.4
djangorestframework-filters==0.11.1
djangorestframework-simplejwt==4.7.2
djoser==2.1.0
idna==3.4
iniconfig==2.0.0
itypes==1.2.0
Jinja2==3.1.2
MarkupSafe==2.1.2
oauthlib==3.2.2
packaging==23.0
Pillow==9.3.0
pluggy==0.13.1
posts==0.2.2
py==1.11.0
pycparser==2.21
PyJWT==2.1.0
pytest==6.2.4
pytest-django==4.4.0
pytest-pythonpath==0.7.3
python3-openid==3.2.0
pytz==2022.7.1
requests==2.26.0
requests-oauthlib==1.3.1
six==1.16.0
social-auth-app-django==4.0.0
social-auth-core==4.3.0
sqlparse==0.4.3
toml==0.10.2
uritemplate==4.1.1
urllib3==1.26.15

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