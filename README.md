# DockerSetUp
#### Create clone:

```
https://github.com/vladislin/elementals-test-task.git
```

#### Create at the root of the project file `.env`, example:

```
DEBUG=1
SECRET_KEY=change_me
DJANGO_ALLOWED_HOSTS=localhost 127.0.0.1 [::1]
SQL_ENGINE=django.db.backends.postgresql
SQL_DATABASE=django_db
SQL_USER=hello_django
SQL_PASSWORD=hello_django
SQL_HOST=db
SQL_PORT=5432
```

#### Up docker-compose:

```
$ docker-compose up -d --build
```

#### Apply migrations and create admin user:

```
$ docker-compose run web python manage.py migrate
$ docker-compose run web python manage.py createsuperuser
```

#### To view docs go to: http://localhost:8000/swagger/


