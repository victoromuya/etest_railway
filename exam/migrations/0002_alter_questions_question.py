# Generated by Django 4.0 on 2022-12-19 09:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exam', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='questions',
            name='question',
            field=models.TextField(default='Enter question'),
        ),
    ]
