# Generated by Django 2.0.7 on 2018-07-31 14:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20180731_1404'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='dislike_ratio',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='like_ratio',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]