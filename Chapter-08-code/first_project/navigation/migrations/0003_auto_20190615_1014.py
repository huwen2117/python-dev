# Generated by Django 2.2.2 on 2019-06-15 02:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('navigation', '0002_auto_20190615_1012'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='likes',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='category',
            name='views',
            field=models.IntegerField(default=0),
        ),
    ]
