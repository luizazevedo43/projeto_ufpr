# Generated by Django 4.2 on 2023-09-11 21:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalogo', '0013_alter_documentofp_data'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='documentofp',
            name='foto',
        ),
        migrations.RemoveField(
            model_name='documentolg',
            name='foto',
        ),
    ]