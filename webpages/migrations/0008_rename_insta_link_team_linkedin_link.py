# Generated by Django 4.0.2 on 2022-07-30 18:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webpages', '0007_about_photo'),
    ]

    operations = [
        migrations.RenameField(
            model_name='team',
            old_name='insta_link',
            new_name='linkedin_link',
        ),
    ]