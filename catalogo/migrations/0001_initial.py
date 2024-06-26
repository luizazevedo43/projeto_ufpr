# Generated by Django 4.2 on 2023-05-04 19:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DocumentoFP',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero', models.CharField(max_length=15)),
                ('tipo', models.CharField(max_length=25)),
                ('titulo', models.CharField(max_length=25)),
                ('remetente', models.TextField()),
                ('destinatario', models.TextField()),
                ('data', models.CharField(max_length=11)),
                ('referencia', models.CharField(max_length=50)),
                ('assunto', models.TextField()),
                ('palavras_chave', models.CharField(max_length=50)),
            ],
        ),
    ]
