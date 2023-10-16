# Django test task

## Описание

Приложение содержит три модели:
1. Album с полем name содержащем название альбома в виде строки, artist указывающий на модель Artist, year год выпуска альбома в виде числа. Модель имеет строковое предавление в виде - name[year]
2. Artist с полем name, содержащем имя автора в виде строки
3. Track с полем name в виде строки, и с полем album указывающий на модель Album

## Установка

```
git clone https://github.com/Alice8080/testdjango.git
```
```
cd testdjango
```
```
pip install -r requirements.txt
```