# Generated by Django 5.0 on 2024-02-21 13:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notex', '0002_useridpas'),
    ]

    operations = [
        migrations.CreateModel(
            name='feedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=300)),
                ('feedback', models.CharField(max_length=5000)),
            ],
        ),
    ]
