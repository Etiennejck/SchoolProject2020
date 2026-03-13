# Generated manually to align model field types after removing PhoneNumberField usage

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('School_Models', '0009_student_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='phone_number',
            field=models.CharField(max_length=128, null=True),
        ),
        migrations.AlterField(
            model_name='parent',
            name='Telephone',
            field=models.CharField(max_length=128, null=True),
        ),
    ]
