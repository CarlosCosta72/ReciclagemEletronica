# Generated by Django 5.2 on 2025-04-07 15:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Componente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100, null = False, blank = False)),
                ('quantidade', models.IntegerField()),
                ('descricao', models.TextField(blank=True, null=True)),
            ],
        ),
    ]
