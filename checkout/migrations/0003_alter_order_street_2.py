# Generated by Django 3.2 on 2022-09-25 14:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0002_alter_orderlineitem_order'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='street_2',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
    ]
