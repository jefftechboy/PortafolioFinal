# Generated by Django 5.2 on 2025-06-01 03:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app", "0009_reserva_precio_total"),
    ]

    operations = [
        migrations.AlterField(
            model_name="reserva",
            name="id_reserva",
            field=models.IntegerField(default=0, primary_key=True, serialize=False),
        ),
    ]
