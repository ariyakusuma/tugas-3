# Generated by Django 4.1 on 2022-09-21 12:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mywatchlist', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movielist',
            name='rating',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='movielist',
            name='release_day',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='movielist',
            name='review',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='movielist',
            name='title',
            field=models.TextField(default=''),
        ),
    ]
