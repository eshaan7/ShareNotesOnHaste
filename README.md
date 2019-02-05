# ShareNotesOnHaste

## New functions

  1. make footer static i.e. not overlapping
  2. add reply functionaity
  3. add edit functionality
  4. add expand func

## Install

Made using [Django](https://www.djangoproject.com/) with [Python 3](https://www.python.org/).

#### How to install on <b>LINUX/MAC</b>

Requirements 
```sh
$ python3 -m venv venv               # CREATE YOUR VENV
$ source venv/bin/activate           # LINUX > ACTIVATE VENV
$ --- / --- / --- / ---- / ----
(venv) $ pip install Django          # INSTALL DJANGO IN VENV
```

#### How to install on <b>Windows</b>

Requirements 
```sh
< C:\USER\DIR > $ python3 -m venv venv          # CREATE YOUR VENV
< C:\USER\DIR > $ venv\scripts\activate.bat     # WINDOWS > ACTIVATE VENV
 --- / --- / --- / ---- / ----
(venv) < C:\USER\DIR > $ pip install Django     # INSTALL DJANGO IN VENV
```

Run project

```sh
(venv) $ cd <directory for download files>
(venv) $ git clone <this repository>
(venv) $ python manage.py migrate
(venv) $ python manage.py createsuperuser
(venv) $ python manage.py runserver
```

[127.0.0.1:8000/login](http://127.0.0.1:8000/login)

```
Note: If you use this project do not forget to change the security key.
```
