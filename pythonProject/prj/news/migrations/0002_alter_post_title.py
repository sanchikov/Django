# Generated by Django 4.1.1 on 2022-10-07 20:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(max_length=128, unique=True),
        ),
    ]
