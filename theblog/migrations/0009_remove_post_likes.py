# Generated by Django 4.1.5 on 2023-07-23 04:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('theblog', '0008_alter_post_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='likes',
        ),
    ]
