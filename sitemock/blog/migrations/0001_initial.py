# Generated by Django 4.1.6 on 2023-02-15 17:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('published_date', models.DateTimeField(auto_created=True, blank=True, null=True, verbose_name='Publicado em')),
                ('created_date', models.DateTimeField(auto_created=True, default=django.utils.timezone.now, verbose_name='Criado em')),
                ('title', models.CharField(max_length=200)),
                ('text', models.TextField()),
                ('updated_at', models.DateTimeField(blank=True, null=True, verbose_name='Atualizado em')),
                ('slug', models.SlugField(blank=True, null=True, unique=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Postagem',
                'verbose_name_plural': 'Postagens',
                'ordering': ['-published_date'],
            },
        ),
    ]
