# Generated by Django 4.1.4 on 2022-12-19 13:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jenfimail', '0007_shipment_arrival_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='line',
            name='description',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
    ]