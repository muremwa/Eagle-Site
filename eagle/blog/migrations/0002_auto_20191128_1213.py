# Generated by Django 2.1.5 on 2019-11-28 09:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='entry',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='blog/entry_images'),
        ),
        migrations.AddField(
            model_name='post',
            name='feature_image',
            field=models.ImageField(default='blog/default_images/default_feature.png', upload_to='blog/feature_images'),
        ),
    ]
