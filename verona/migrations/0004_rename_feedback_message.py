# Generated by Django 3.2.7 on 2021-09-01 23:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('verona', '0003_feedback'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Feedback',
            new_name='Message',
        ),
    ]
