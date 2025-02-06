# Generated by Django 5.1.4 on 2025-01-16 17:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_event_image_alter_event_date_alter_event_location'),
    ]

    operations = [
        migrations.CreateModel(
            name='DirectorsMessage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message_text', models.TextField()),
                ('image', models.ImageField(blank=True, null=True, upload_to='director_images/')),
                ('quote', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.DeleteModel(
            name='DirectorMessage',
        ),
    ]
