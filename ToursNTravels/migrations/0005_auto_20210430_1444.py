
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ToursNTravels', '0004_purchase_type'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='purchase',
            name='bookingID',
        ),
        migrations.AlterField(
            model_name='purchase',
            name='Type',
            field=models.CharField(default='', max_length=10, null=True),
        ),
        migrations.DeleteModel(
            name='booking',
        ),
    ]
