

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

```
    python manage.py test

```

# Features
- Tokens
- Postgresql
- Django
- Django REST Framework
- Funcionalidad de días de reserva *calcular
- Entrypoint para inicializar
- Tests

```
Client
{
    "identification": "2879592",
    "name": "Ricardo",
    "ruc": "2879592-0"
}

Person
{
    "id": 1,
    "identification": "2879592",
    "name": "SOLE MOLINAS",
    "age": 31
},
{
    "id": 2,
    "identification": "23123123",
    "name": "RICARDO MOLINAS",
    "age": 31
}

Room
{
    "number": "10",
    "bed_qty": 2,
    "price": 15.0
}
{
    "id": 2,
    "number": "11",
    "bed_qty": 2,
    "price": 15.0
}


Reserva
{
    "status": "pendiente",
    "days": 12,
    "person": [
        1
    ],
    "client": 1,
    "date_initial": "2022-07-20T13:58:00Z",
    "date_finished": "2022-07-21T13:59:00Z",
    "room_ids": 1,
    "amount_total": "312122"

```


