# Generated by Django 5.0.7 on 2024-08-06 17:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medicSearch', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
