# Generated by Django 3.0.4 on 2020-03-19 13:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('business', '0014_auto_20200317_1403'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='name_de',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='category',
            name='name_en',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='category',
            name='name_fr',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='category',
            name='name_it',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
