# Generated by Django 4.1.6 on 2023-02-12 17:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_alter_post_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='slug',
            field=models.SlugField(blank=True, null=True, unique=True),
        ),
    ]