# Generated by Django 5.0.7 on 2024-10-30 10:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='OrderTbl',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Quantity', models.IntegerField()),
                ('TotalPrice', models.IntegerField()),
                ('date', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=100)),
                ('Category', models.CharField(max_length=50)),
                ('Quantity', models.IntegerField()),
                ('Price', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='SupplierTbl',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=100)),
                ('Contact', models.CharField(max_length=100)),
            ],
        ),
    ]
