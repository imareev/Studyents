# Generated by Django 4.2.6 on 2023-12-13 12:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapi', '0004_alter_module_number_of_tests'),
    ]

    operations = [
        migrations.AlterField(
            model_name='test',
            name='number_of_completed_tasks',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='test',
            name='number_of_tasks',
            field=models.IntegerField(default=0),
        ),
    ]
