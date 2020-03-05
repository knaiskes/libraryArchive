# libraryArchive
A Web application to model a simple library archiving system

## Quick Start

### Clone project

```
$ git clone https://github.com/KNaiskes/libraryArchive
```

### Create - activate virtual enviroment and install dependencies

```
$ cd libraryArchive/
$ python -m venv venv
$ source venv/bin/activate
$ pip install -r requirements.txt
```

## Migrate database models

```
$ cd libraryArchive/
$ python manage.py makemigrations books authors
$ python manage.py migrate
```

## Create admin user (for admin panel)

```
$ python manage.py createsuperuser
```
When you start the project (next step) you will be able to
navigate to [localhost:8000/admin](localhost:8000/admin) and add books and authors

## Start project

```
$ python manage.py runserver
```
