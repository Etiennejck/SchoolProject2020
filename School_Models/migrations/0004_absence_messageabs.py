# Generated by Django 2.2.16 on 2020-09-14 10:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('School_Models', '0003_remove_level_id_classdiary'),
    ]

    operations = [
        migrations.AddField(
            model_name='absence',
            name='messageAbs',
            field=models.TextField(null=True),
        ),
    ]