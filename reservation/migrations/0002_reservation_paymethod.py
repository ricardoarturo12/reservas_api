# Generated by Django 4.0.6 on 2022-07-22 00:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservation', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='reservation',
            name='paymethod',
            field=models.CharField(choices=[('efectivo', 'efectivo'), ('tarjeta', 'tarjeta'), ('transferencia', 'transferencia'), ('otro', 'otro')], default='tarjeta', max_length=20),
        ),
    ]
