# Generated by Django 4.2.6 on 2023-10-11 10:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Device',
            fields=[
                ('id', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('deviceModel', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=50)),
                ('note', models.TextField(blank=True)),
                ('serial', models.CharField(max_length=100)),
            ],
        ),
    ]
