# Generated by Django 5.0.4 on 2024-04-17 07:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('estudiantes', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pago',
            name='C_banco',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='pago',
            name='N_boleta',
            field=models.IntegerField(),
        ),
    ]
