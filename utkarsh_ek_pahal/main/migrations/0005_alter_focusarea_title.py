# Generated by Django 5.1.4 on 2025-01-18 07:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_focusarea'),
    ]

    operations = [
        migrations.AlterField(
            model_name='focusarea',
            name='title',
            field=models.CharField(max_length=100),
        ),
    ]
