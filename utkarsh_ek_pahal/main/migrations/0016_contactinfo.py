# Generated by Django 5.1.4 on 2025-01-21 17:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0015_alter_heroslider_button_link_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(blank=True, max_length=15, null=True)),
                ('address', models.TextField()),
                ('message', models.TextField(blank=True, null=True)),
            ],
        ),
    ]
