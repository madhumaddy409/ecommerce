# Generated by Django 3.1 on 2020-10-02 14:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0002_auto_20201002_2023'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='username',
        ),
    ]