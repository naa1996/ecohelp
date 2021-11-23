# Generated by Django 3.2.8 on 2021-11-10 07:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('todo', '0022_alter_task_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='creator_user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL, verbose_name='Создатель'),
        ),
    ]