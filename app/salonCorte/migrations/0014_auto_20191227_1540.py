# Generated by Django 2.2.4 on 2019-12-27 18:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('salonCorte', '0013_auto_20191227_1422'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tintura',
            name='gramo',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='tintura',
            name='marca',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
