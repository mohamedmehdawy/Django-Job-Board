# Generated by Django 4.0.3 on 2022-03-24 15:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0017_job_owner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='slug',
            field=models.SlugField(blank=True, null=True, unique=True),
        ),
    ]
