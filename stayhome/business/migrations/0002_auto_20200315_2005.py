# Generated by Django 3.0.4 on 2020-03-15 20:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('geodata', '0008_auto_20200315_1940'),
        ('business', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='business',
            name='location',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='geodata.NPA'),
        ),
    ]