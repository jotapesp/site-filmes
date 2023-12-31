# Generated by Django 4.2.3 on 2023-07-13 19:58

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("filmesfav", "0008_alter_ator_falecimento_alter_ator_nascimento_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="ator",
            name="falecimento",
            field=models.DateField(
                blank=True,
                default=datetime.datetime(2023, 7, 13, 19, 58, 18, 132381),
                help_text="Data de falecimento (caso esteja vivo, deixe em branco).",
                null=True,
                verbose_name="Data de falecimento",
            ),
        ),
        migrations.AlterField(
            model_name="ator",
            name="nascimento",
            field=models.DateField(
                default=datetime.datetime(2023, 7, 13, 19, 58, 18, 132376),
                help_text="Data de nascimento",
                verbose_name="Data de nascimento",
            ),
        ),
        migrations.AlterField(
            model_name="diretor",
            name="falecimento",
            field=models.DateField(
                blank=True,
                default=datetime.datetime(2023, 7, 13, 19, 58, 18, 132138),
                help_text="Data de falecimento (caso esteja vivo, deixe em branco).",
                null=True,
                verbose_name="Data de falecimento",
            ),
        ),
        migrations.AlterField(
            model_name="diretor",
            name="nascimento",
            field=models.DateField(
                default=datetime.datetime(2023, 7, 13, 19, 58, 18, 132127),
                help_text="Data de nascimento.",
                verbose_name="Data de nascimento",
            ),
        ),
        migrations.AlterField(
            model_name="filme",
            name="data",
            field=models.DateField(
                default=datetime.datetime(2023, 7, 13, 19, 58, 18, 132643),
                help_text="Data de estreia",
            ),
        ),
        migrations.AlterField(
            model_name="filme",
            name="elenco",
            field=models.ManyToManyField(related_name="filmes", to="filmesfav.ator"),
        ),
        migrations.AlterField(
            model_name="filme",
            name="genero",
            field=models.ManyToManyField(related_name="filmes", to="filmesfav.genero"),
        ),
    ]
