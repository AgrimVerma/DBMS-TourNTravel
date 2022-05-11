from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ToursNTravels', '0007_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='purchase',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
