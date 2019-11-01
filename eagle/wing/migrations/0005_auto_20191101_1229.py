# Generated by Django 2.1.5 on 2019-11-01 09:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wing', '0004_eagledetails'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='eagledetails',
            options={'verbose_name': 'Super Details', 'verbose_name_plural': 'Eagle Details'},
        ),
        migrations.AlterField(
            model_name='eagledetails',
            name='portrait',
            field=models.ImageField(upload_to='eagle_details/'),
        ),
        migrations.AlterField(
            model_name='portfolio',
            name='portfolio_type',
            field=models.CharField(max_length=300),
        ),
    ]
