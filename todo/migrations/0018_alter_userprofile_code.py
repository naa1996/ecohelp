# Generated by Django 3.2.8 on 2021-10-28 20:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0017_auto_20211029_0129'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='code',
            field=models.IntegerField(default='0000', editable=False, verbose_name='Код'),
        ),
    ]