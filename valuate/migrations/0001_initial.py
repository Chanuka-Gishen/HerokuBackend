# Generated by Django 3.0.5 on 2021-04-22 21:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserValuationDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('size', models.CharField(max_length=50)),
                ('land_type', models.CharField(max_length=50)),
                ('distance_to_town', models.CharField(max_length=50)),
                ('calculate_year', models.CharField(max_length=4)),
                ('lane', models.CharField(max_length=50)),
                ('predicted_value', models.CharField(max_length=50)),
            ],
        ),
    ]
