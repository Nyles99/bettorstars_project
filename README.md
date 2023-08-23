# bettorstars_project
Приложения для спорах о спорте с друзьями

Скачать приложение через SSH
Зайти в папку bettorstars_project и установить виртуальное окружение: <br>
1. python -m venv venv

Активировать его: <br>
2. source venv/scripts/activate

Обновить виртуальное окружение: <br>
3. python -m pip install --upgrade pip

Установить зависимости из файла requirements.txt: <br>
4. pip install -r requirements.txt

Выполнить миграции: <br>
5. python manage.py migrate

Запустить проект: <br>
6. python manage.py runserver
