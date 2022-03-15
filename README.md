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



