# bettorstars_project
Приложения для спорах о спорте с друзьями

Скачать приложение через SSH
Зайти в папку bettorstars_project и установить виртуальное окружение:
1. python -m venv venv

Активировать его:
2. source venv/bin/activate

Установить зависимости из файла requirements.txt:
3. pip install -r requirements.txt

Выполнить миграции:
4. python manage.py migrate

Запустить проект:
5. python manage.py runserver
