# Generated by Django 4.2 on 2023-09-15 20:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalogo', '0018_remove_documentolg_usuario_documentolg_added_by'),
    ]

    operations = [
        migrations.RenameField(
            model_name='documentolg',
            old_name='added_by',
            new_name='usuario',
        ),
    ]