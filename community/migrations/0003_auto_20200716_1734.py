# Generated by Django 3.0.8 on 2020-07-16 08:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('community', '0002_dislikes_likes_viewed'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comments',
            old_name='author',
            new_name='user',
        ),
        migrations.RenameField(
            model_name='dislikes',
            old_name='author',
            new_name='user',
        ),
        migrations.RenameField(
            model_name='likes',
            old_name='author',
            new_name='user',
        ),
        migrations.RenameField(
            model_name='viewed',
            old_name='author',
            new_name='user',
        ),
    ]
