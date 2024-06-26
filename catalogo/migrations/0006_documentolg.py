# Generated by Django 4.2 on 2023-05-05 19:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalogo', '0005_documentofp_foto'),
    ]

    operations = [
        migrations.CreateModel(
            name='DocumentoLG',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('entidade_origem', models.CharField(max_length=25)),
                ('numero', models.CharField(max_length=25)),
                ('data', models.CharField(max_length=11)),
                ('ementa', models.CharField(blank=True, max_length=50, null=True)),
                ('assinatura', models.CharField(max_length=50)),
                ('assunto', models.CharField(blank=True, max_length=50, null=True)),
                ('referencia', models.CharField(max_length=50)),
                ('local', models.CharField(max_length=50)),
                ('palavras_chave', models.CharField(max_length=50)),
                ('responsavel', models.CharField(max_length=50)),
            ],
        ),
    ]
