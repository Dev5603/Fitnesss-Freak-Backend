# Generated by Django 5.1.3 on 2024-11-12 05:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('API', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Membership',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('amount', models.CharField(max_length=6)),
            ],
        ),
        migrations.CreateModel(
            name='PT',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('type', models.CharField(choices=[('GOLD', 'Gold'), ('DIAMOND', 'Diamond')], max_length=10)),
                ('amount', models.CharField(max_length=6)),
            ],
        ),
    ]
