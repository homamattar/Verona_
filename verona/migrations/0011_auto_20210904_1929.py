# Generated by Django 3.2.7 on 2021-09-04 19:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('verona', '0010_auto_20210904_1859'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='name',
        ),
        migrations.AddField(
            model_name='project',
            name='file',
            field=models.FileField(default='url', upload_to='images/', verbose_name='File'),
        ),
    ]
