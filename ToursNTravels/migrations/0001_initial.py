
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='booking',
            fields=[
                ('id', models.IntegerField(auto_created=True, primary_key=True, serialize=False, unique=True)),
                ('startDate', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='flight',
            fields=[
                ('id', models.IntegerField(auto_created=True, primary_key=True, serialize=False, unique=True)),
                ('departureDate', models.DateField()),
                ('sourceLocation', models.CharField(max_length=30)),
                ('destinationLocation', models.CharField(max_length=30)),
                ('fareEconomy', models.DecimalField(decimal_places=2, max_digits=6)),
                ('fareBusiness', models.DecimalField(decimal_places=2, max_digits=6)),
                ('fareFirst', models.DecimalField(decimal_places=2, max_digits=6)),
                ('numSeatsRemainingEconomy', models.IntegerField()),
                ('numSeatsRemainingBusiness', models.IntegerField()),
                ('numSeatsRemainingFirst', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='hotel',
            fields=[
                ('id', models.IntegerField(auto_created=True, primary_key=True, serialize=False, unique=True)),
                ('dailyCost', models.DecimalField(decimal_places=2, max_digits=6)),
                ('address', models.CharField(max_length=30)),
                ('city', models.CharField(max_length=30)),
                ('companyName', models.CharField(default='hotel', max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='location',
            fields=[
                ('id', models.IntegerField(auto_created=True, primary_key=True, serialize=False, unique=True)),
                ('city', models.CharField(max_length=30)),
                ('region', models.CharField(max_length=2)),
                ('country', models.CharField(default='US', max_length=2)),
            ],
        ),
        migrations.CreateModel(
            name='payment',
            fields=[
                ('id', models.IntegerField(auto_created=True, primary_key=True, serialize=False, unique=True)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=6)),
                ('paymentType', models.CharField(choices=[('credit', 'Credit'), ('debit', 'Debit')], max_length=6)),
                ('cardNo', models.CharField(max_length=16)),
            ],
        ),
        migrations.CreateModel(
            name='train',
            fields=[
                ('id', models.IntegerField(auto_created=True, primary_key=True, serialize=False, unique=True)),
                ('departureDate', models.DateField()),
                ('sourceLocation', models.CharField(max_length=30)),
                ('destinationLocation', models.CharField(max_length=30)),
                ('fareEconomy', models.DecimalField(decimal_places=2, max_digits=6)),
                ('fareBusiness', models.DecimalField(decimal_places=2, max_digits=6)),
                ('fareFirst', models.DecimalField(decimal_places=2, max_digits=6)),
                ('numSeatsRemainingEconomy', models.IntegerField()),
                ('numSeatsRemainingBusiness', models.IntegerField()),
                ('numSeatsRemainingFirst', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='user',
            fields=[
                ('username', models.CharField(max_length=40)),
                ('email', models.CharField(max_length=35, primary_key=True, serialize=False, unique=True)),
                ('password', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='review',
            fields=[
                ('id', models.IntegerField(auto_created=True, primary_key=True, serialize=False, unique=True)),
                ('rating', models.IntegerField()),
                ('review', models.CharField(max_length=1000)),
                ('submissionDate', models.DateField(auto_now=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ToursNTravels.user')),
            ],
        ),
        migrations.CreateModel(
            name='purchase',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('transactionDate', models.DateTimeField(auto_now=True)),
                ('bookingID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ToursNTravels.booking')),
                ('paymentID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ToursNTravels.payment')),
                ('userID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ToursNTravels.user')),
            ],
        ),
        migrations.AddField(
            model_name='booking',
            name='Flight',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='ToursNTravels.flight'),
        ),
        migrations.AddField(
            model_name='booking',
            name='Train',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='ToursNTravels.train'),
        ),
        migrations.CreateModel(
            name='attraction',
            fields=[
                ('id', models.IntegerField(auto_created=True, primary_key=True, serialize=False, unique=True)),
                ('attractionName', models.CharField(max_length=30)),
                ('attractionDescription', models.CharField(max_length=1000)),
                ('image', models.CharField(max_length=200)),
                ('location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ToursNTravels.location')),
            ],
        ),
    ]
