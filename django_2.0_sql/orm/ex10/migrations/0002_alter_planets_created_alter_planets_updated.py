# Generated by Django 5.1.7 on 2025-03-24 15:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ex10', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='planets',
            name='created',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='planets',
            name='updated',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]
