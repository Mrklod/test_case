# Generated by Django 4.1.7 on 2023-04-05 14:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_users_point'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='point',
            field=models.FloatField(default=0),
        ),
    ]