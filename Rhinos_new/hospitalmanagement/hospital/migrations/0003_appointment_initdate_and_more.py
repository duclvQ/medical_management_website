# Generated by Django 4.0.4 on 2022-07-29 08:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospital', '0002_patientdischargedetails'),
    ]

    operations = [
        migrations.AddField(
            model_name='appointment',
            name='initDate',
            field=models.DateField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='appointment',
            name='appointmentDate',
            field=models.DateField(),
        ),
    ]