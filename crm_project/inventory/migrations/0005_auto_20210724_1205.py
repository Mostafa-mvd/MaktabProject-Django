# Generated by Django 3.2.5 on 2021-07-24 12:05

from django.db import migrations, models
import inventory.fields


class Migration(migrations.Migration):

    dependencies = [
        ('organization', '0004_auto_20210724_1158'),
        ('inventory', '0004_alter_product_pdf_catalog'),
    ]

    operations = [
        migrations.CreateModel(
            name='CompanyProduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='نام محصول')),
                ('has_taxation', models.BooleanField(default=True, verbose_name='آیا مشمول مالیات است؟')),
                ('image_catalog', models.ImageField(blank=True, upload_to='media/catalogs/pictures', verbose_name='عکس کاتالوگ')),
                ('pdf_catalog', inventory.fields.PdfField(blank=True, upload_to='media/catalogs/pdfs', verbose_name='پی دی اف کاتالوگ')),
                ('price', models.PositiveIntegerField(verbose_name='قیمت')),
                ('technical_features', models.TextField(max_length=300, verbose_name='ویژگی های فنی')),
                ('related_with_manufacturedـproducts', models.ManyToManyField(to='organization.OrganizationProduct', verbose_name='قابل استفاده برای تولید محصولات تولیدی')),
            ],
        ),
        migrations.DeleteModel(
            name='Product',
        ),
    ]
