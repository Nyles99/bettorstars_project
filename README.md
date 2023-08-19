# bettorstars_project
Приложения для спорах о спорте с друзьями

Скачать приложение через SSH
Зайти в папку bettorstars_project и установить виртуальное окружение:
1. python -m venv venv

Активировать его:
2. source venv/bin/activate

Обновить виртуальное окружение:
3. python -m pip install --upgrade pip

Установить зависимости из файла requirements.txt:
4. pip install -r requirements.txt

Выполнить миграции:
5. python manage.py migrate

Запустить проект:
6. python manage.py runserver
