# Generated by Django 4.2 on 2023-04-28 21:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0006_remove_area_parent_area_delete_button'),
    ]

    operations = [
        migrations.AddField(
            model_name='postagem',
            name='slug',
            field=models.SlugField(default='postagem-sem-titulo', unique=True),
        ),
    ]
