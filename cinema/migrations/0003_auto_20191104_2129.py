# Generated by Django 2.2.6 on 2019-11-04 21:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cinema', '0002_auto_20191104_1645'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='seat',
            name='is_available',
        ),
        migrations.CreateModel(
            name='SeatInEvent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_available', models.BooleanField(default=False)),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='selected_event', to='cinema.Event')),
                ('seat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='selected_seat', to='cinema.Seat')),
            ],
        ),
    ]
