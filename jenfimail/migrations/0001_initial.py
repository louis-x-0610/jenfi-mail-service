# Generated by Django 4.1.4 on 2022-12-12 11:22

from django.db import migrations, models
import django.db.models.deletion
import django_fsm


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Line',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
                ('description', models.CharField(max_length=250)),
                ('available', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Parcel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(max_length=100)),
                ('weight', models.FloatField()),
                ('volume', models.FloatField()),
                ('description', models.CharField(max_length=250)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('is_withdrawn', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Shipment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('departure_date', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Train',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('cost', models.FloatField()),
                ('weight_capacity', models.FloatField()),
                ('volume_capacity', models.FloatField()),
                ('status', django_fsm.FSMField(choices=[('open', 'open'), ('booked', 'booked'), ('withdrawn', 'withdrawn')], default='open', max_length=50, protected=True)),
            ],
        ),
        migrations.CreateModel(
            name='TrainLine',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('line', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='jenfimail.line')),
                ('train', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='jenfimail.train')),
            ],
        ),
        migrations.AddField(
            model_name='train',
            name='lines',
            field=models.ManyToManyField(related_name='trains', through='jenfimail.TrainLine', to='jenfimail.line'),
        ),
        migrations.CreateModel(
            name='ShipmentParcel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('porcel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='jenfimail.parcel')),
                ('shipment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='jenfimail.shipment')),
            ],
        ),
        migrations.AddField(
            model_name='shipment',
            name='parcels',
            field=models.ManyToManyField(related_name='shipments', through='jenfimail.ShipmentParcel', to='jenfimail.parcel'),
        ),
        migrations.AddField(
            model_name='shipment',
            name='train',
            field=models.OneToOneField(on_delete=django.db.models.deletion.RESTRICT, to='jenfimail.train'),
        ),
        migrations.AddField(
            model_name='parcel',
            name='shipment',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.RESTRICT, to='jenfimail.shipment'),
        ),
        migrations.AddIndex(
            model_name='parcel',
            index=models.Index(fields=['created_at'], name='jenfimail_p_created_bd51b9_idx'),
        ),
    ]