# Django test task

## Описание

Приложение содержит три модели:
1. Album с полями name - название альбома в виде строки, artist - указывает на модель Artist, year - год выпуска альбома в виде числа. Модель имеет строковое предавление в виде name[year].
2. Artist с полем name, содержащим имя автора в виде строки.
3. Track с полем name в виде строки и полем album, которое указывает на модель Album.

## Установка и запуск

```
git clone https://github.com/Alice8080/testdjango.git
```
```
cd testdjango
```
```
python -m venv venv
```
```
# cmd.exe
venv\Scripts\activate.bat
# PowerShell
venv\Scripts\Activate.ps1
# Linux
source venv/bin/activate
```
```
pip install -r requirements.txt
```
```
python manage.py migrate
```
```
python manage.py runserver
```
Приложение будет доступно по адресу [http://localhost:8000](http://localhost:8000).

## Функционал

После запуска на главной станице приложения будут доступны формы добавления артистов, альбомов, треков. Чтобы добавить альбом, сначала нужно создать артиста; чтобы добавить трек, нужно сначала создать альбом. 

API приложения доступно по адресу [http://localhost:8000/api/data](http://localhost:8000/api/data), через него доступны данные приложения в виде списка словарей: [{
"album": "album1[2022]", "name": "album1",
"artist@name": "artist_name1",
"tracks": ["track1", "track2", "track3"]
}, ...
]

При передаче параметра sorting (пример: [http://localhost:8000/api/data?sorting=name](http://localhost:8000/api/data?sorting=name)) сортировка списка осуществляется по указанному параметру. Если передан параметр, которого нет в ключах словарей, сортировка осуществляется по дефолтному параметру (name). 

Логика API с комментариями описана в файле [views.py](https://github.com/Alice8080/testdjango/blob/main/app/views.py)

Созданы [тесты](https://github.com/Alice8080/testdjango/blob/main/app/tests.py) для добавления данных и получения данных через API с параметром sorting и без. Запуск тестов:
```
python manage.py test
```