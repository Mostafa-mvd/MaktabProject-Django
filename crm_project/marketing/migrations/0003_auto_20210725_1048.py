# Generated by Django 3.2.5 on 2021-07-25 10:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('marketing', '0002_rename_quoteitems_quoteitem'),
    ]

    operations = [
        migrations.RenameField(
            model_name='quoteitem',
            old_name='qty',
            new_name='quantity',
        ),
        migrations.RenameField(
            model_name='quoteitem',
            old_name='Quote',
            new_name='quote',
        ),
    ]
