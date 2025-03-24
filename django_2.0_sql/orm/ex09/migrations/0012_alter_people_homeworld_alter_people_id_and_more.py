# Generated by Django 5.1.7 on 2025-03-24 13:50

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ex09', '0011_alter_people_birth_year_alter_people_eye_color_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='people',
            name='homeworld',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='ex09.planets'),
        ),
        migrations.AlterField(
            model_name='people',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='people',
            name='name',
            field=models.CharField(max_length=64),
        ),
        migrations.AlterField(
            model_name='planets',
            name='climate',
            field=models.CharField(null=True),
        ),
        migrations.AlterField(
            model_name='planets',
            name='diameter',
            field=models.BigIntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='planets',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='planets',
            name='orbital_period',
            field=models.BigIntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='planets',
            name='terrain',
            field=models.CharField(null=True),
        ),
    ]
