# Generated by Django 4.0.4 on 2022-04-12 15:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=15)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.IntegerField()),
                ('number_of_number', models.IntegerField()),
                ('date', models.DateField()),
                ('time', models.TimeField()),
            ],
            options={
                'verbose_name': 'Reservation',
                'verbose_name_plural': 'Reservations',
            },
        ),
    ]