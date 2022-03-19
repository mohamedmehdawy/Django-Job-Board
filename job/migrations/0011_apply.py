# Generated by Django 4.0.3 on 2022-03-16 17:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0010_job_slug'),
    ]

    operations = [
        migrations.CreateModel(
            name='Apply',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('website', models.URLField()),
                ('cv', models.FileField(upload_to='apply/')),
                ('coverletter', models.TextField(max_length=200)),
            ],
        ),
    ]
