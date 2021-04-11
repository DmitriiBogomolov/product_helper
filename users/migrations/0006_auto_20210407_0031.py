# Generated by Django 3.1.7 on 2021-04-06 14:31

import django.core.validators
from django.db import migrations, models
import users.validators


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_remove_user_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(max_length=35, unique=True, validators=[django.core.validators.EmailValidator(message='Введите корректрый email адрес.')], verbose_name='Email'),
        ),
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.TextField(max_length=12, unique=True, validators=[users.validators.validate_username], verbose_name='Логин'),
        ),
    ]
