# Generated by Django 3.2.7 on 2021-12-15 18:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0003_delete_localname'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='fruit',
            name='country',
        ),
    ]
