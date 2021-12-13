# Generated by Django 3.2.9 on 2021-12-13 11:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='vendorprofile',
            options={'verbose_name_plural': 'Vendor Profiles'},
        ),
        migrations.AlterField(
            model_name='vendorprofile',
            name='store_owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='vendorprofile', to='profiles.userprofile'),
        ),
    ]
