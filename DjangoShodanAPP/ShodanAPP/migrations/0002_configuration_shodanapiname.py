# Generated by Django 4.1.1 on 2022-09-12 18:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ShodanAPP', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='configuration',
            name='ShodanAPIName',
            field=models.CharField(default='ShodanAPI', max_length=30),
        ),
    ]