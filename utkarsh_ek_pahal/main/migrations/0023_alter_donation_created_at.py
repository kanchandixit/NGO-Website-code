from django.db import migrations, models
import django.utils.timezone

def set_default_created_at(apps, schema_editor):
    Donation = apps.get_model('main', 'Donation')
    for donation in Donation.objects.filter(created_at__isnull=True):
        donation.created_at = django.utils.timezone.now()
        donation.save()

class Migration(migrations.Migration):

    dependencies = [
        ('main', '0022_rename_donor_name_donation_payment_id_and_more'),  # Change this to 0022
    ]

    operations = [
        migrations.AlterField(
            model_name='donation',
            name='created_at',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.RunPython(set_default_created_at),
    ]
