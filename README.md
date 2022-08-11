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
cd {program_directory_on_your_local_disk}
python manage.py runserver 0.0.0.0:8000
```
The website will only work if you have access to the database.
The main page of the site can be found at http://127.0.0.1:8000/

### Project data

To run a project with your own data, you need to add a `project/.env` file to access the database like this:
```
#
DATABASE_URL=postgres://{user}:{password}@{hostname}:{port}/{database-name}
SECRET_KEY={secret_key}
ALLOWED_HOSTS={allowed_hosts}
DEBUG={debug_mode}
```
For example:
```
#
DATABASE_URL=postgres://username:password@localhost:5432/marketing
SECRET_KEY=replace_me
ALLOWED_HOSTS=example.com,awesomedomain.com,10.0.0.2
DEBUG=True
```

### Project Goals

The code is written for educational purposes in the process of learning on the online course on Django ORM for Python developers.