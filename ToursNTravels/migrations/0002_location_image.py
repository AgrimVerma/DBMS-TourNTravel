

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('ToursNTravels', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='location',
            name='image',
            field=models.CharField(default=django.utils.timezone.now, max_length=200),
            preserve_default=False,
        ),
    ]
