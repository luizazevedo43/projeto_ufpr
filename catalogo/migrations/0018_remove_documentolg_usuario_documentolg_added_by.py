# Generated by Django 4.2 on 2023-09-15 20:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('catalogo', '0017_documentofp_usuario_documentolg_usuario'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='documentolg',
            name='usuario',
        ),
        migrations.AddField(
            model_name='documentolg',
            name='added_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
    ]
