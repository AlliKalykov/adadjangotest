# Generated by Django 4.2.1 on 2023-05-17 05:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0005_secondmodel_eight_secondmodel_five_secondmodel_nine_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='modelname',
            old_name='birth_date',
            new_name='birthday',
        ),
    ]
