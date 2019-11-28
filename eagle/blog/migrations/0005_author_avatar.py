# Generated by Django 2.1.5 on 2019-11-28 12:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_post_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='avatar',
            field=models.ImageField(default='blog/default_images/default_author_avatar.png', upload_to='blog/authors_avatars/'),
        ),
    ]