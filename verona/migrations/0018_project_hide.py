# Generated by Django 3.2.7 on 2021-09-05 23:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('verona', '0017_auto_20210904_2219'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='hide',
            field=models.BooleanField(default=False),
        ),
    ]