# Generated by Django 5.1.7 on 2025-04-07 18:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='works',
            name='salary',
            field=models.IntegerField(),
        ),
    ]
