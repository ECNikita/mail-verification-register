# Generated by Django 3.2.8 on 2021-11-02 04:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BarvaAPI', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ChartModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Product_id', models.BigIntegerField()),
                ('datefrom', models.DateTimeField()),
                ('dateto', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='ChartResponseModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.IntegerField()),
                ('quantity', models.IntegerField()),
                ('datefrom', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Lotunit_masterModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Lotunit_id', models.BigIntegerField(blank=True, null=True)),
                ('Lotunit_name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Producer_masterModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Producer_id', models.BigIntegerField(blank=True, null=True)),
                ('Producer_name', models.CharField(max_length=100)),
                ('Producer_address', models.CharField(max_length=100)),
                ('Producer_mobileno', models.IntegerField()),
                ('Producer_adhaarno', models.BigIntegerField(blank=True, null=True)),
                ('Producer_email', models.CharField(max_length=100)),
                ('Producer_pancard', models.CharField(max_length=100)),
                ('Producer_gstno', models.BigIntegerField(blank=True, null=True)),
                ('Producer_firmregistration', models.BigIntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Product_masterModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Product_id', models.BigIntegerField(blank=True, null=True)),
                ('Product_name', models.CharField(max_length=100)),
                ('Product_size', models.CharField(max_length=100)),
                ('Product_season', models.CharField(max_length=100)),
                ('Product_fractionalreserve', models.BigIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Product_pricebyproducerModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Product_id', models.BigIntegerField(blank=True, null=True)),
                ('Producer_id', models.BigIntegerField(blank=True, null=True)),
                ('price', models.IntegerField(blank=True, null=True)),
                ('datefrom', models.DateTimeField()),
                ('dateto', models.DateTimeField()),
                ('Lotunit_id', models.BigIntegerField(blank=True, null=True)),
                ('quantity', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Trader_detailsModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Trader_id', models.BigIntegerField(blank=True, null=True)),
                ('Traderrole_id', models.BigIntegerField(blank=True, null=True)),
                ('Trader_name', models.CharField(max_length=100)),
                ('Trader_email', models.CharField(max_length=100)),
                ('Trader_mobile', models.BigIntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='TraderroleModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Traderrole_id', models.BigIntegerField(blank=True, null=True)),
                ('Traderrole_name', models.CharField(max_length=100)),
            ],
        ),
        migrations.RenameField(
            model_name='register_details',
            old_name='Company',
            new_name='Firm',
        ),
        migrations.RenameField(
            model_name='register_details',
            old_name='CompanyAddress',
            new_name='FirmAddress',
        ),
    ]
