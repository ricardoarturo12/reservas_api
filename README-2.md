### Django - Docker-compose

https://docs.docker.com/samples/django/

Tests
https://developer.mozilla.org/es/docs/Learn/Server-side/Django/Testing


## pasos

```
    docker-compose run web python manage.py startapp reservation
```

```
    docker-compose run web makemigrations
    docker-compose run web migrate
    docker-compose run web python manage.py createsuperuser
```


# Features
- Tokens
- Funcionalidad de días de reserva *calcular
- Entrypoint para inicializar
- Tests


