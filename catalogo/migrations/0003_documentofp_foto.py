# Generated by Django 4.2 on 2023-05-04 22:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalogo', '0002_alter_documentofp_numero'),
    ]

    operations = [
        migrations.AddField(
            model_name='documentofp',
            name='foto',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
