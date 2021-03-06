# Generated by Django 2.2.16 on 2020-09-03 07:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('School_Models', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='meal',
            name='id_School',
        ),
        migrations.RemoveField(
            model_name='schoolpg',
            name='id_event',
        ),
        migrations.RemoveField(
            model_name='schoolpg',
            name='id_meal',
        ),
        migrations.RemoveField(
            model_name='schoolpg',
            name='id_rules',
        ),
        migrations.AddField(
            model_name='event',
            name='id_School',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='School_Models.SchoolPg'),
        ),
        migrations.AddField(
            model_name='inscription',
            name='id_School',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='School_Models.SchoolPg'),
        ),
        migrations.AddField(
            model_name='room_type',
            name='name',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='rules',
            name='id_School',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='School_Models.SchoolPg'),
        ),
    ]
