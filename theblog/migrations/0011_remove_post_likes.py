# Generated by Django 4.1.5 on 2023-07-23 05:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('theblog', '0010_post_likes'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='likes',
        ),
    ]