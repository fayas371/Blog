# Generated by Django 4.1.5 on 2023-07-24 04:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('theblog', '0014_post_snippet'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='header_image',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]