# Generated by Django 3.2.23 on 2023-11-07 06:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecom', '0005_feedback_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='sales_count',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='customer',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='feedback',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='orders',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='product',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
