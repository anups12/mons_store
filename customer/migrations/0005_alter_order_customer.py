# Generated by Django 4.0.1 on 2022-05-15 08:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0004_shipping_name_shipping_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='customer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='customer.customer'),
        ),
    ]
