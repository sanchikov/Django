# Generated by Django 4.1.3 on 2022-11-07 11:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='rating',
            field=models.SmallIntegerField(default=0),
        ),
    ]
