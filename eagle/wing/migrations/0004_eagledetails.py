# Generated by Django 2.1.5 on 2019-11-01 09:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wing', '0003_portfolio'),
    ]

    operations = [
        migrations.CreateModel(
            name='EagleDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bio', models.TextField()),
                ('portrait', models.ImageField(upload_to='', verbose_name='eagle_details/')),
                ('address', models.CharField(max_length=500)),
                ('phone', models.CharField(max_length=10)),
                ('facebook', models.URLField(blank=True, null=True)),
                ('twitter', models.URLField(blank=True, null=True)),
                ('email', models.EmailField(max_length=254)),
                ('website', models.URLField()),
            ],
        ),
    ]
