# Generated by Django 4.0.3 on 2022-03-16 17:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0011_apply'),
    ]

    operations = [
        migrations.AlterField(
            model_name='apply',
            name='coverletter',
            field=models.TextField(max_length=500),
        ),
        migrations.AlterField(
            model_name='apply',
            name='email',
            field=models.EmailField(max_length=100),
        ),
    ]
