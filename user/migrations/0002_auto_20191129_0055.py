# Generated by Django 2.2.7 on 2019-11-28 19:25

from django.db import migrations, models
import django_countries.fields
import django_mysql.models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='follower',
        ),
        migrations.RemoveField(
            model_name='user',
            name='following',
        ),
        migrations.RemoveField(
            model_name='user',
            name='profile_pic',
        ),
        migrations.RemoveField(
            model_name='user',
            name='tags',
        ),
        migrations.AddField(
            model_name='user',
            name='bio',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AddField(
            model_name='user',
            name='blockList',
            field=django_mysql.models.ListCharField(models.CharField(default='', max_length=25), default='', max_length=2500000, size=10000),
        ),
        migrations.AddField(
            model_name='user',
            name='message',
            field=models.CharField(default='', max_length=2000),
        ),
        migrations.AlterField(
            model_name='user',
            name='country',
            field=django_countries.fields.CountryField(blank=True, default='', max_length=2),
        ),
    ]
