# Generated by Django 4.0.6 on 2022-07-20 22:26

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('identification', models.CharField(max_length=255, unique=True)),
                ('name', models.CharField(max_length=255)),
                ('ruc', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('identification', models.CharField(max_length=255, unique=True)),
                ('name', models.CharField(max_length=255)),
                ('age', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.CharField(max_length=255, unique=True)),
                ('bed_qty', models.PositiveIntegerField()),
                ('price', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hash_reservation', models.UUIDField(default=uuid.uuid4, editable=False)),
                ('status', models.CharField(choices=[('pendiente', 'pendiente'), ('pagado', 'pagado'), ('eliminado', 'eliminado')], default='pendiente', max_length=10)),
                ('days', models.PositiveIntegerField()),
                ('date_initial', models.DateTimeField()),
                ('date_finished', models.DateTimeField()),
                ('amount_total', models.CharField(max_length=255, null=True)),
                ('client_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='reservation.client')),
                ('persons', models.ManyToManyField(to='reservation.person')),
                ('room_id', models.ManyToManyField(to='reservation.room')),
            ],
        ),
    ]
