# Generated by Django 3.2.7 on 2021-09-04 19:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('verona', '0012_auto_20210904_1932'),
    ]

    operations = [
        migrations.RenameField(
            model_name='project',
            old_name='file',
            new_name='main_photo',
        ),
    ]
