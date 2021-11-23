# Generated by Django 3.2.8 on 2021-11-12 09:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('todo', '0025_auto_20211112_1452'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='creator_user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, to='auth.user', verbose_name='Создатель'),
            preserve_default=False,
        ),
    ]