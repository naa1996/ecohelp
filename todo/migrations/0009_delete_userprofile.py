# Generated by Django 3.2.8 on 2021-11-05 14:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0008_alter_userprofile_options'),
    ]

    operations = [
        migrations.DeleteModel(
            name='UserProfile',
        ),
    ]