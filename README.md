https://github.com/veromanich/kittygram_final/actions/workflows/main.yml/badge.svg

# kittygram_final
### Описание:
Kittygram — социальная сеть для обмена фотографиями любимых питомцев. Это полностью рабочий проект, который состоит из бэкенд-приложения на Django и фронтенд-приложения на React.
##
### Стек технологий:
<details>
<summary>Подробнее/свернуть</summary>

- Python 3.9
- Django 3.2.3
- React
- DRF
- Djoser
</details>

##
### Установка:
<details>
<summary>Подробнее/свернуть</summary>
  
Клонировать репозиторий и перейти в него в командной строке:
```
git clone https://github.com/veromanich/kittygram_final.git
```
```
cd kittygram_final
```
Cоздать и активировать виртуальное окружение:
```
python3 -m venv env
```
```
source env/bin/activate
```
Установить зависимости из файла requirements.txt:
```
python3 -m pip install --upgrade pip
```
```
pip install -r requirements.txt
```
Выполнить миграции:
```
python3 manage.py migrate
```
В корне проекта создать файл .env:
```
touch .env
```
Добавить в .env следующие переменные:
```
POSTGRES_DB=kittygram
POSTGRES_USER=kittygram_user
POSTGRES_PASSWORD=kittygram_password
DB_NAME=kittygram
DB_HOST=db
DB_PORT=5432
SECRET_KEY=
DEBUG=# True/False
ALLOWED_HOSTS=127.0.0.1,localhost
```
Запустить проект:
```
python3 manage.py runserver
```
</details>

##
### Автор:
[Роман Веренич](https://github.com/veromanich)