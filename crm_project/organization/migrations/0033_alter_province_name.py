# Generated by Django 3.2.5 on 2021-07-28 20:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organization', '0032_auto_20210728_1112'),
    ]

    operations = [
        migrations.AlterField(
            model_name='province',
            name='name',
            field=models.CharField(max_length=50, unique=True, verbose_name='استان'),
        ),
    ]
