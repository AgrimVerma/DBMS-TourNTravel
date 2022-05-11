#

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ToursNTravels', '0003_auto_20210430_1140'),
    ]

    operations = [
        migrations.AddField(
            model_name='purchase',
            name='Type',
            field=models.CharField(default='', max_length=10),
        ),
    ]
