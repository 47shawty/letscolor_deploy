# Generated by Django 3.1 on 2021-10-21 21:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0003_brand_brandtranslation'),
        ('store', '0003_auto_20211021_0030'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='brand',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='category.brand', verbose_name='Brand'),
        ),
    ]
