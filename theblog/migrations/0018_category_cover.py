# Generated by Django 4.1.5 on 2023-07-25 04:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('theblog', '0017_userprofile_instagram_url_userprofile_linkedin_url_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='cover',
            field=models.ImageField(blank=True, null=True, upload_to='cover/'),
        ),
    ]
