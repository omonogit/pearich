# Generated by Django 4.1.5 on 2023-06-06 00:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posApp', '0005_sales_valid_to'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sales',
            name='valid_to',
        ),
        migrations.AddField(
            model_name='products',
            name='quantity',
            field=models.IntegerField(blank=True, default='0', null=True),
        ),
        migrations.AddField(
            model_name='products',
            name='valid_to',
            field=models.DateTimeField(null=True),
        ),
    ]
