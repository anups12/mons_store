# Generated by Django 4.0.4 on 2022-05-08 09:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('seller', '0002_rename_username_seller_user_alter_seller_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='brand',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='seller.brand'),
        ),
    ]
