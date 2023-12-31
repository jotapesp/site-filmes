# Generated by Django 4.2.3 on 2023-07-13 16:43

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("filmesfav", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="ator",
            name="nascimento",
            field=models.DateTimeField(
                default=datetime.datetime(2023, 7, 13, 16, 43, 31, 260175),
                help_text="Data de nascimento",
                verbose_name="Data de nascimento",
            ),
        ),
        migrations.AlterField(
            model_name="diretor",
            name="nascimento",
            field=models.DateTimeField(
                default=datetime.datetime(2023, 7, 13, 16, 43, 31, 260045),
                help_text="Data de nascimento",
                verbose_name="Data de nascimento",
            ),
        ),
        migrations.AlterField(
            model_name="filmes",
            name="data",
            field=models.DateTimeField(
                default=datetime.datetime(2023, 7, 13, 16, 43, 31, 259432),
                help_text="Data de estreia",
            ),
        ),
    ]
