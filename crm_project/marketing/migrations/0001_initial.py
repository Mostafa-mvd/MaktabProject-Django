# Generated by Django 3.2.5 on 2021-07-24 13:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('inventory', '0005_auto_20210724_1205'),
        ('organization', '0007_alter_organization_expert_creator'),
    ]

    operations = [
        migrations.CreateModel(
            name='Quote',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_time', models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ایجاد پیش فاکتور')),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='organization.organization', verbose_name='سازمان')),
            ],
        ),
        migrations.CreateModel(
            name='QuoteItems',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('qty', models.PositiveIntegerField(default=1, verbose_name='تعداد خرید')),
                ('price', models.PositiveIntegerField(default=0, verbose_name='قیمت محصول')),
                ('discount', models.FloatField(default=0.0, verbose_name='تخفیف')),
                ('Quote', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='marketing.quote')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='inventory.companyproduct')),
            ],
        ),
    ]
