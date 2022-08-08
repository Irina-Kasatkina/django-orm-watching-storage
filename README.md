# Bank security datacenter

This is an internal repository for Siyanie bank employees. If you got into this repository by accident, then you will not be able to run it, because. you do not have access to the database, but you can freely use the web layout code or see how the database queries are implemented.

The security console is a website that can be connected to a remote database with visits and pass cards of our bank employees.

### How to install

To install the project, copy it to your local drive.

You should already have Python3 installed.<br>
It's best to work in a virtual environment to avoid conflicts with your version of Django.<br>
Then use `pip` (or `pip3`, there is a conflict with Python2) to install the dependencies:
```
pip install -r requirements.txt
```

### How to start

Run cmd, change to the program directory on the command line, then start local server:
```
cd <program_directory_on_your_local_disk>
python manage.py runserver 0.0.0.0:8000
```
The website will only work if you have access to the database.
The main page of the site can be found at http://127.0.0.1:8000/

### Project Goals

The code is written for educational purposes in the process of learning on the online course on Django ORM for Python developers.

### Project Goals

The code is written for educational purposes on online-course for web-developers [dvmn.org](https://dvmn.org/).



# Пульт охраны банка

Это внутренний репозиторий для сотрудников банка "Сияние". Если вы попали в этот репозиторий случайно, то вы не сможете его запустить, т.к. у вас нет доступа к БД, но можете свободно использовать код вёрстки или посмотреть, как реализованы запросы к БД.

Пульт охраны - это сайт, который можно подключить к удалённой базе данных с визитами и карточками пропуска сотрудников нашего банка.

### Как установить

Для установки проекта скопируйте его на свой локальный диск.

У вас уже должен быть установлен Python3.<br>
Лучше работать в виртуальном окружении, чтобы избежать конфликта с установленной у вас версией Django.<br>
Затем используйте `pip` (или `pip3`, есть конфликт с Python2) для установки зависимостей:
```
pip install -r requirements.txt
```

### Как запустить

Запустите cmd, в командной строке перейдите в каталог программы, затем запустите локальный сервер:
```
cd <каталог_программы_на_вашем_локальном_диске>
python manage.py runserver 0.0.0.0:8000
```
Сайт будет работать, только если у вас есть доступ к БД.
Главную страницу сайта можно будет найти по адресу http://127.0.0.1:8000/

### Цель проекта

Код написан в учебных целях в процессе обучения на онлайн-курсе по Django ORM для Python-разработчиков.