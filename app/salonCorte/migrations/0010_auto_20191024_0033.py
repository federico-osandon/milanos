# Generated by Django 2.2.4 on 2019-10-24 03:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('salonCorte', '0009_auto_20191024_0031'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tintura',
            old_name='color',
            new_name='nombre',
        ),
    ]