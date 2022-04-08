# Generated by Django 3.2.7 on 2021-09-04 19:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('verona', '0011_auto_20210904_1929'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='name',
            field=models.CharField(default='Project', max_length=64),
        ),
        migrations.AlterField(
            model_name='project',
            name='file',
            field=models.FileField(upload_to='images/', verbose_name='File'),
        ),
    ]
