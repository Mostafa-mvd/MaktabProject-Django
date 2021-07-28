# Generated by Django 3.2.5 on 2021-07-28 11:12

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organization', '0031_auto_20210728_1109'),
    ]

    operations = [
        migrations.AlterField(
            model_name='organization',
            name='organization_phone_number',
            field=models.CharField(max_length=11, unique=True, validators=[django.core.validators.RegexValidator(message="organization's phone number is invalid", regex='^(\\+98|0)?\\d{1,2}\\d{1,8}$')], verbose_name='شماره تلفن سازمان'),
        ),
        migrations.AlterField(
            model_name='organization',
            name='owner_phone_number',
            field=models.CharField(max_length=11, unique=True, validators=[django.core.validators.RegexValidator(message="owner's phone number is invalid", regex='^(\\+98|0)?9\\d{9}$')], verbose_name='شماره تلفن مخاطب'),
        ),
    ]
