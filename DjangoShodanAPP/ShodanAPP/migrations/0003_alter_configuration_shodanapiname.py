# Generated by Django 4.1.1 on 2022-09-12 18:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ShodanAPP', '0002_configuration_shodanapiname'),
    ]

    operations = [
        migrations.AlterField(
            model_name='configuration',
            name='ShodanAPIName',
            field=models.CharField(default='ShodanAPIKey', max_length=30),
        ),
    ]