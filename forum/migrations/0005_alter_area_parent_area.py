# Generated by Django 4.2 on 2023-04-27 21:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0004_area_parent_area'),
    ]

    operations = [
        migrations.AlterField(
            model_name='area',
            name='parent_area',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='subareas', to='forum.area'),
        ),
    ]
