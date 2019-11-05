# Generated by Django 2.2.6 on 2019-11-05 10:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('street1', models.CharField(blank=True, max_length=300)),
                ('street2', models.CharField(max_length=300)),
                ('houseNumber', models.CharField(max_length=300)),
                ('city', models.CharField(max_length=300)),
                ('psc', models.CharField(max_length=30)),
            ],
        ),
    ]