# Generated by Django 3.1.3 on 2020-11-17 20:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Passengers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('First_Name', models.CharField(max_length=20)),
                ('Last_Name', models.CharField(max_length=20)),
                ('Birth', models.DateField()),
                ('Passport_Number', models.CharField(max_length=8)),
            ],
        ),
        migrations.CreateModel(
            name='Flights',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Flight_Number', models.CharField(max_length=8)),
                ('Departure', models.CharField(max_length=50)),
                ('Destination', models.CharField(max_length=50, null=True)),
                ('Departure_date', models.DateField()),
                ('Return_date', models.DateField(blank=True)),
                ('CarryOn', models.IntegerField(blank=True)),
                ('Trolley', models.IntegerField(blank=True)),
                ('CheckIn', models.IntegerField(blank=True)),
                ('PassangerId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.passengers')),
            ],
        ),
    ]
