# Generated by Django 5.0.1 on 2024-01-26 08:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Stocks', '0013_rename_high_price_stockdata_ema_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='stockdata',
            name='rs',
            field=models.DecimalField(decimal_places=4, max_digits=10, null=True),
        ),
        migrations.AddField(
            model_name='stockdata',
            name='rsi',
            field=models.DecimalField(decimal_places=4, max_digits=10, null=True),
        ),
    ]
