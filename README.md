# newspaper_app
### Развёртывание
-Установить docker и docker-compose
-Склонировать проект
-Зайти в папку с проектом и выполнить комманду "sudo docker-compose build"
-Выполнить команду "sudo docker-compose run web python manage.py makemigrations"
-Выполнить команду "sudo docker-compose run web python manage.py migrate"
-Выполнить команду "sudo docker-compose up"
