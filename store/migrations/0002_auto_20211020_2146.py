# Generated by Django 3.1 on 2021-10-20 16:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='category.category', verbose_name='Category'),
        ),
        migrations.AlterField(
            model_name='product',
            name='created_date',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Created Date'),
        ),
        migrations.AlterField(
            model_name='product',
            name='image_change',
            field=models.ImageField(blank=True, null=True, upload_to='photos/products', verbose_name='Image Change'),
        ),
        migrations.AlterField(
            model_name='product',
            name='images',
            field=models.ImageField(upload_to='photos/products', verbose_name='Images'),
        ),
        migrations.AlterField(
            model_name='product',
            name='is_available',
            field=models.BooleanField(default=True, verbose_name='Is Available'),
        ),
        migrations.AlterField(
            model_name='product',
            name='modified_date',
            field=models.DateTimeField(auto_now=True, verbose_name='Modified Date'),
        ),
        migrations.AlterField(
            model_name='product',
            name='old_price',
            field=models.IntegerField(default=0, verbose_name='Old Price'),
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.IntegerField(verbose_name='Price'),
        ),
        migrations.AlterField(
            model_name='product',
            name='slug',
            field=models.SlugField(max_length=200, unique=True, verbose_name='Slug'),
        ),
        migrations.AlterField(
            model_name='product',
            name='stock',
            field=models.IntegerField(verbose_name='Stock'),
        ),
        migrations.AlterField(
            model_name='productgallery',
            name='image',
            field=models.ImageField(max_length=255, upload_to='store/products', verbose_name='Image'),
        ),
        migrations.AlterField(
            model_name='productgallery',
            name='product',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='store.product', verbose_name='Product'),
        ),
        migrations.AlterField(
            model_name='producttranslation',
            name='description',
            field=models.TextField(blank=True, max_length=1500, verbose_name='Description'),
        ),
        migrations.AlterField(
            model_name='producttranslation',
            name='product_name',
            field=models.CharField(max_length=200, unique=True, verbose_name='Product Name'),
        ),
        migrations.AlterField(
            model_name='producttranslation',
            name='short_description',
            field=models.TextField(blank=True, max_length=255, verbose_name='Short Description'),
        ),
        migrations.AlterField(
            model_name='reviewrating',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Created At'),
        ),
        migrations.AlterField(
            model_name='reviewrating',
            name='ip',
            field=models.CharField(blank=True, max_length=20, verbose_name='IP'),
        ),
        migrations.AlterField(
            model_name='reviewrating',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.product', verbose_name='Product'),
        ),
        migrations.AlterField(
            model_name='reviewrating',
            name='rating',
            field=models.FloatField(verbose_name='Rating'),
        ),
        migrations.AlterField(
            model_name='reviewrating',
            name='review',
            field=models.TextField(blank=True, max_length=500, verbose_name='Review'),
        ),
        migrations.AlterField(
            model_name='reviewrating',
            name='status',
            field=models.BooleanField(default=True, verbose_name='Status'),
        ),
        migrations.AlterField(
            model_name='reviewrating',
            name='subject',
            field=models.CharField(blank=True, max_length=100, verbose_name='Subject'),
        ),
        migrations.AlterField(
            model_name='reviewrating',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, verbose_name='Updated At'),
        ),
        migrations.AlterField(
            model_name='reviewrating',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='User'),
        ),
        migrations.AlterField(
            model_name='variation',
            name='created_date',
            field=models.DateTimeField(auto_now=True, verbose_name='Created Date'),
        ),
        migrations.AlterField(
            model_name='variation',
            name='is_active',
            field=models.BooleanField(default=True, verbose_name='Is Active'),
        ),
        migrations.AlterField(
            model_name='variation',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.product', verbose_name='Product'),
        ),
        migrations.AlterField(
            model_name='variation',
            name='variation_category',
            field=models.CharField(choices=[('color', 'color'), ('size', 'size')], max_length=100, verbose_name='Variation Category'),
        ),
        migrations.AlterField(
            model_name='variationtranslation',
            name='variation_value',
            field=models.CharField(max_length=100, verbose_name='Variation Value'),
        ),
    ]
