# Generated by Django 3.1 on 2021-11-15 10:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_auto_20211026_1413'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='phone_number',
            field=models.CharField(blank=True, max_length=50, null=True, unique=True, verbose_name='Phone Number'),
        ),
    ]
