# Generated by Django 5.0.6 on 2024-07-29 11:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('solar_app', '0005_alter_mysolarrr_production_alter_mysolarrr_total'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mysolarrr',
            name='bkk',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='mysolarrr',
            name='production',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='mysolarrr',
            name='total',
            field=models.IntegerField(),
        ),
    ]