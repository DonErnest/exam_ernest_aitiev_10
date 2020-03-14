# Generated by Django 2.2.7 on 2020-03-14 04:19

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0003_sharedfile_privately_accessed'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sharedfile',
            name='privately_accessed',
            field=models.ManyToManyField(blank=True, related_name='private_files', to=settings.AUTH_USER_MODEL, verbose_name='Приватный доступ'),
        ),
    ]
