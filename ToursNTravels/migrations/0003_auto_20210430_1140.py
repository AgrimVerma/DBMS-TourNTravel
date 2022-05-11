
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ToursNTravels', '0002_location_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='Flight',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='ToursNTravels.flight'),
        ),
        migrations.AlterField(
            model_name='booking',
            name='Train',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='ToursNTravels.train'),
        ),
    ]
