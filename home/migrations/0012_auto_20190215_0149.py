# Generated by Django 2.1.7 on 2019-02-15 01:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0011_comment_parents'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='mainpage',
            field=models.IntegerField(blank=True),
        ),
    ]
