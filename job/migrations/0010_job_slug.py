# Generated by Django 4.0.3 on 2022-03-14 16:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0009_rename_vacancy_job_vacancy'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='slug',
            field=models.SlugField(blank=True, null=True),
        ),
    ]