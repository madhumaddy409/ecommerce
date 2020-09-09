# Generated by Django 3.1 on 2020-08-31 20:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=60)),
                ('description', models.CharField(max_length=250)),
                ('availability', models.CharField(max_length=35)),
                ('image', models.CharField(max_length=35)),
                ('ratings', models.DecimalField(decimal_places=5, max_digits=30)),
                ('price', models.BigIntegerField()),
                ('brand', models.CharField(max_length=35)),
            ],
        ),
    ]
