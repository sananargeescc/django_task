# Generated by Django 4.1.4 on 2023-01-31 06:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('studentapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mark',
            name='roll_number',
            field=models.IntegerField(default=0, unique=True),
        ),
    ]