# Generated by Django 5.2 on 2025-05-31 21:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app", "0003_habitacion_imagen"),
    ]

    operations = [
        migrations.AlterField(
            model_name="habitacion",
            name="descripcion",
            field=models.TextField(max_length=500),
        ),
    ]
