# Generated by Django 4.2 on 2023-04-27 18:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='area',
            name='title',
            field=models.CharField(default='', max_length=100),
        ),
    ]
