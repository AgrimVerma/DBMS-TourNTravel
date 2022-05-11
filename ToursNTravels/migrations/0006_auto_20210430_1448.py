

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ToursNTravels', '0005_auto_20210430_1444'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='attraction',
            name='location',
        ),
        migrations.DeleteModel(
            name='flight',
        ),
        migrations.DeleteModel(
            name='hotel',
        ),
        migrations.RemoveField(
            model_name='purchase',
            name='paymentID',
        ),
        migrations.RemoveField(
            model_name='purchase',
            name='userID',
        ),
        migrations.RemoveField(
            model_name='review',
            name='author',
        ),
        migrations.DeleteModel(
            name='train',
        ),
        migrations.DeleteModel(
            name='attraction',
        ),
        migrations.DeleteModel(
            name='location',
        ),
        migrations.DeleteModel(
            name='payment',
        ),
        migrations.DeleteModel(
            name='purchase',
        ),
        migrations.DeleteModel(
            name='review',
        ),
        migrations.DeleteModel(
            name='user',
        ),
    ]
