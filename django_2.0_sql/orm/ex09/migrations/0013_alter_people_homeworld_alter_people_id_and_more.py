# Generated by Django 5.1.7 on 2025-03-24 14:00

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ex09', '0012_alter_people_homeworld_alter_people_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='people',
            name='homeworld',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='ex09.planets'),
        ),
        migrations.AlterField(
            model_name='people',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='people',
            name='name',
            field=models.CharField(max_length=64, unique=True),
        ),
        migrations.AlterField(
            model_name='planets',
            name='climate',
            field=models.CharField(max_length=128, null=True),
        ),
        migrations.AlterField(
            model_name='planets',
            name='diameter',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='planets',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='planets',
            name='orbital_period',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='planets',
            name='terrain',
            field=models.CharField(max_length=128, null=True),
        ),
    ]
