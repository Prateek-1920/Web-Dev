# Generated by Django 5.1.7 on 2025-04-07 18:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company_app', '0002_alter_works_salary'),
    ]

    operations = [
        migrations.AlterField(
            model_name='works',
            name='salary',
            field=models.FloatField(),
        ),
    ]
