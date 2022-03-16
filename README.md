# sber_study

Требуется создать файл `.env` в `sber_study` (рядом с `settings.py`). 
С содержимым:
```
SECRET_KEY=XXXXX
DEBUG=on
SQL_DEBUG=on
ALLOWED_HOSTS=*
DATABASE_URL=psql://username:password@localhost:5432/db_name
```

Установить зависимости:
```
# Лучше взять python^=3.8
pip install -r requirements.txt
```

Выполнить миграции
```
python manage.py migrate
```


Создать суперюзера
```
python manage.py createsuperuser
```


[Админка](http://127.0.0.1:8000/admin/) \
[API документация](http://127.0.0.1:8000/docs/)


По заданию:
1) Предварительно занести данные. Можно через админку для удобства или воспользоваться API
2) CRUD операции реализованы. Лучше смотреть их в [API документация](http://127.0.0.1:8000/docs/)
3) Вывод предметов по направлению.
   1) Перейти на http://127.0.0.1:8000/study/subjects/
   2) Нажать на "Фильтры" и выбрать направление
   3) Или в ручную прописать фильтр: http://127.0.0.1:8000/study/subjects/?direction=1
4) Тесты лежат тут: study/tests/test_views.py + рядом фабрики
