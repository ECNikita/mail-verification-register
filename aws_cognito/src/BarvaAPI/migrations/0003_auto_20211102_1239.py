# Generated by Django 3.2.8 on 2021-11-02 07:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BarvaAPI', '0002_auto_20211102_1005'),
    ]

    operations = [
        migrations.CreateModel(
            name='Traderrole_Model',
            fields=[
                ('Traderrole_id', models.BigIntegerField(blank=True, null=True, primary_key=True, serialize=False)),
                ('Traderrole_name', models.CharField(max_length=100)),
            ],
        ),
        migrations.DeleteModel(
            name='TraderroleModel',
        ),
        migrations.RemoveField(
            model_name='product_pricebyproducermodel',
            name='id',
        ),
        migrations.AddField(
            model_name='product_pricebyproducermodel',
            name='Serial_id',
            field=models.BigIntegerField(blank=True, null=True, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='producer_mastermodel',
            name='Producer_adhaarno',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='producer_mastermodel',
            name='Producer_firmregistration',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='producer_mastermodel',
            name='Producer_gstno',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='producer_mastermodel',
            name='Producer_mobileno',
            field=models.CharField(max_length=100),
        ),
    ]
