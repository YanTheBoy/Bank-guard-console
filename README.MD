# Bank guard console

The local repository for bank 'Siyanie' employees. If you accidentally get in the repository, you can`t
launch this console, because you dont have database access. But you can using layout code or look how to
get requests to database.

Guard console - the site, which could be connected with remote database with visits and passcards of all our bank employees.

# How to install
Make a request to database from your bank manager. For access ypu need: port, host, name, user, password.
You should put 'port', 'name' , 'user' data in settings.py.
 ```bash
...
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'HOST': os.getenv('DB_HOST'),
        'PORT': your port,
        'NAME': your name,
        'USER': yout user,
        'PASSWORD': os.getenv('DB_PASSWORD')
    }
}
``` 
Your 'host' and 'password' put in .env file in local folder:
```text
DB_PASSWORD=your password
DB_HOST=your host
```
Python3 should be already installed. Then use pip (or pip3, if there is a conflict with Python2) to install dependencies:
```bash
$ pip install -r requirements.txt
```
Run manage.py for creating your local connection:
```bash
$ python3 manage.py runserver
Performing system checks...
System check identified no issues (0 silenced).
April 21, 2020 - 12:47:53
Django version 1.11, using settings 'project.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.
```

# Project Goals
The code is written for educational purposes on online-course for web-developers [DEVMAN.org](https://devman.org)