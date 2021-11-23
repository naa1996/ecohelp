# Generated by Django 3.2.8 on 2021-11-16 19:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('todo', '0033_alter_task_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='TaskDone',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(upload_to='', verbose_name='Фото')),
                ('task', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='todo.task', verbose_name='Задание')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
        ),
    ]