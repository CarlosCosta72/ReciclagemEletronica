# Generated by Django 5.2 on 2025-04-10 19:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('estoque', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='componente',
            name='quantidade',
            field=models.IntegerField(default=0),
        ),
    ]
