# Generated by Django 2.1.2 on 2018-10-22 08:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('server', '0009_symptom'),
    ]

    operations = [
        migrations.AddField(
            model_name='appointment',
            name='symptom',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]