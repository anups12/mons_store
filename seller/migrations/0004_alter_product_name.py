# Generated by Django 4.0.4 on 2022-05-12 19:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('seller', '0003_alter_product_brand'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.CharField(max_length=120),
        ),
    ]