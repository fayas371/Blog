# Generated by Django 4.1.5 on 2023-07-23 16:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('theblog', '0013_alter_post_body'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='snippet',
            field=models.CharField(default='The blog snipet', max_length=100),
        ),
    ]
