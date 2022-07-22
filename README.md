
# Reservations API

## Documentation

[Django](https://www.djangoproject.com/)
Django makes it easier to build better web apps more quickly and with less code.

[Django-rest-framework](https://www.django-rest-framework.org)
Django REST framework is a powerful and flexible toolkit for building Web APIs.

[Postgresql](https://www.postgresql.org)
PostgreSQL is a powerful, open source object-relational database system.
## Demo

Link to demo

http://181.120.120.83:8000/api/

## API Reference

### Person
#### Get all persons

```http
  GET /api/person/
```

#### Get a person

```http
  GET /api/person/${id}/
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `id`      | `string` | **Required**. Id of person to fetch |


#### Post a person

```http
  POST /api/person/
```
| Parameter             | Type      | Description                       |
| :--------             | :-------  | :-------------------------------- |
| `identification`      | `string`  | **Required**. **Unique**          |
| `name`                | `string`  | **Required**.                     |
| `age`                 | `integer` | **Required**.                     |


### Client

#### Post a client

```http
  POST /api/client/
```
| Parameter          | Type      | Description                       |
| :--------          | :-------  | :-------------------------------- |
| `identification`   | `string`  | **Required**. **Unique**          |
| `name`             | `string`  | **Required**.                     |
| `ruc`              | `string`  | **Required**.                     |


#### Get a client

```http
  GET /api/client/${id}/
```

| Parameter | Type     | Description                          |
| :-------- | :------- | :--------------------------------    |
| `id`      | `string` | **Required**. Id of client to fetch  |



### Room

#### Post a room

```http
  POST /api/room/
```
| Parameter    | Type      | Description                       |
| :--------    | :-------  | :-------------------------------- |
| `number`     | `string`  | **Required**. **Unique**          |
| `bed_qty`    | `integer` | **Required**                      |
| `price`      | `float`   | **Required**                      |    

#### Get a room

```http
  GET /api/room/${id}/
```

| Parameter | Type     | Description                          |
| :-------- | :------- | :--------------------------------    |
| `id`      | `string` | **Required**. Id of room to fetch  |


### Reservations
#### Post a reservation

```http
  POST /api/reservation/
```
| Parameter       | Type           | Description                                                |
| :--------       | :-------       | :--------------------------------                          |
| `status`        | `string`       | **Required** ('pendiente','pagado', 'eliminado')           |
| `days`          | `integer`      | **Required**                                               |    
| `date_initial`  | `date_time`    | **Required**                                               |    
| `date_finished` | `date_time`    | **Required**                                               |    
| `persons`       | `many_to_many` | **Required**                                               |    
| `client_id`     | `many_to_one`  |                                                            |    
| `room_id`       | `many_to_many` | **Required**                                               |    
| `paymethod`     | `string`       | **Required**('efectivo','tarjeta','transferencia','otro')  |    
| `amount_total`  | `float`        | **Required**                                               |    


#### Get reservations

```http
  GET /api/reservation/
```

| Parameter           | Type           | Description                        |
| :--------           | :-------       | :--------------------------------  |
| `id`                | `integer`      | **optional**                       |
| `hash_reservation`  | `uuid`         | **optional**                       |    


#### Get a reservation
```http
  GET /api/reservation/{id}/
```

| Parameter           | Type           | Description                        |
| :--------           | :-------       | :--------------------------------  |
| `id`                | `integer`      | **optional**                       |


## Deployment

To deploy this project run

```bash
  docker-compose up
```

#### Create user admin

```bash
docker-compose run web python manage.py createsuperuser
```


## Running Tests

To run tests, run the following command

```bash
  docker-compose run web python manage.py test
```


## Environment Variables

To run this project, you will need to add the following environment variables to your .env file

`POSTGRES_NAME=`

`POSTGRES_USER=`

`POSTGRES_PASSWORD=`

`SECRET_KEY=`

## Usage/Examples

#### Client
```json
{
    "identification": "2879592",
    "name": "Ricardo",
    "ruc": "2879592-0"
}
```

#### Person
```json
{
    "identification": "2879592",
    "name": "SOLE MOLINAS",
    "age": 31
}

```

#### Room
```json
{
    "number": "10",
    "bed_qty": 2,
    "price": 15.0
}
```

#### Reserva
```json
{
    "status": "pendiente",
    "days": 12,
    "date_initial": "2022-07-20T18:35:42Z",
    "date_finished": "2022-07-20T18:35:44Z",
    "amount_total": 12312.0,
    "paymethod": "tarjeta",
    "client_id": {
            "identification": "2879592",
            "name": "Ricardo",
            "ruc": "2879592-0"
    },
    "persons": [
        {
            "identification": "2879592",
            "name": "SOLE MOLINAS",
            "age": 31
        }
    ],
    "room_ids": [
        {
            "number": "10"
        }
    ]
}
```

## Improve

- Tokens
- Funcionalidad calcular cantidad de días
- Actualización de datos de persona
- Test Reservation views
- Implementar https://swagger.io/ para documentar


## Review

#### Reservación
La reservación tiene los siguientes campos:
- Estado: Pendiente, pagado y eliminado.
- Días.
- Fecha inicial y final.
- Monto total.
- Método de pago: Efectivo, tarjeta, transferencia, otro.
- Cliente: Es el cliente a facturar. Debe estar ingresado previamente para envío de datos (no requerido).
- Personas: La reserva se puede realizar para varias personas. Si la persona no está registrada, se registra en el endpoint.
- Habitaciones: La reserva se puede realizar para una o varias habitaciones.
- Hash: Código generado para identificación de reserva.


#### Persona
- Identificación (Documento de identidad)
- Nombre
- Edad

### Cliente a facturar
- Identificación (Documento de identidad), si es empresa (Documento tributario).
- Nombre
- RUC (Documento tributario).

### Habitación
- Número
- Cantidad de camas
- Precio
