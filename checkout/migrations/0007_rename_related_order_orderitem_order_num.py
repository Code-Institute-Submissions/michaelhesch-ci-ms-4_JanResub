# Generated by Django 3.2.9 on 2021-12-08 22:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0006_order_shipping'),
    ]

    operations = [
        migrations.RenameField(
            model_name='orderitem',
            old_name='related_order',
            new_name='order_num',
        ),
    ]