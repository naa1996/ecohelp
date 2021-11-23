# Generated by Django 3.2.8 on 2021-11-12 10:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0028_status_status_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='status',
            name='status_id',
        ),
        migrations.AlterField(
            model_name='task',
            name='status',
            field=models.ForeignKey(default='Ожидание', on_delete=django.db.models.deletion.DO_NOTHING, to='todo.status', verbose_name='Статус'),
        ),
    ]