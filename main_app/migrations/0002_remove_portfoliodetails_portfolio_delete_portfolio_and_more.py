# Generated by Django 5.1.5 on 2025-02-03 13:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='portfoliodetails',
            name='portfolio',
        ),
        migrations.DeleteModel(
            name='Portfolio',
        ),
        migrations.DeleteModel(
            name='PortfolioDetails',
        ),
    ]
