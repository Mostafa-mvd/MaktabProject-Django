# Generated by Django 3.2.5 on 2021-07-21 14:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organization', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='organization',
            name='manufacturedـproducts',
            field=models.ManyToManyField(to='organization.OrganizationProduct', verbose_name='محصولات تولیدی'),
        ),
    ]
