# Generated by Django 2.1.7 on 2019-02-14 23:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prestasi', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='postingprestasi',
            name='statuspublih',
            field=models.BooleanField(default=False),
        ),
    ]
