# Generated by Django 4.2.1 on 2023-05-17 05:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0006_rename_birth_date_modelname_birthday'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='secondmodel',
            name='five',
        ),
    ]
