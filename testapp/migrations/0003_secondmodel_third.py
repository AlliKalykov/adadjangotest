# Generated by Django 4.2.1 on 2023-05-17 05:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0002_secondmodel_first_secondmodel_second'),
    ]

    operations = [
        migrations.AddField(
            model_name='secondmodel',
            name='third',
            field=models.CharField(default='default value', max_length=50),
        ),
    ]
