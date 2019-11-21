# Generated by Django 2.1.5 on 2019-11-21 19:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wing', '0005_auto_20191101_1229'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserMessage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('subject', models.CharField(max_length=400)),
                ('message', models.TextField()),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
