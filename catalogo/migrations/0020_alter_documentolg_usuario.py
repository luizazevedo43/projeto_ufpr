# Generated by Django 4.2 on 2023-09-15 21:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('catalogo', '0019_rename_added_by_documentolg_usuario'),
    ]

    operations = [
        migrations.AlterField(
            model_name='documentolg',
            name='usuario',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='usuariolg', to=settings.AUTH_USER_MODEL),
        ),
    ]