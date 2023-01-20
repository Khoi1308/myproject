# Generated by Django 4.1.3 on 2022-12-26 04:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('idpd', models.CharField(max_length=5, primary_key=True, serialize=False)),
                ('namepd', models.CharField(blank=True, max_length=1000, null=True)),
                ('typepd', models.CharField(blank=True, max_length=30, null=True)),
                ('price', models.CharField(blank=True, max_length=15, null=True)),
                ('amount', models.IntegerField(blank=True, null=True)),
                ('branch', models.CharField(blank=True, max_length=40, null=True)),
                ('descript', models.TextField(blank=True, null=True)),
                ('imgpd', models.ImageField(default=True, upload_to='images')),
            ],
            options={
                'db_table': 'PRODUCT',
            },
        ),
        migrations.CreateModel(
            name='RegistetUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(blank=True, max_length=100, null=True)),
                ('email', models.CharField(blank=True, max_length=100, null=True)),
                ('password', models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                'db_table': 'RegistetUser',
            },
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('idsv', models.CharField(max_length=3, primary_key=True, serialize=False)),
                ('namesv', models.CharField(blank=True, max_length=40, null=True)),
                ('price', models.CharField(blank=True, max_length=10, null=True)),
                ('name', models.CharField(max_length=128)),
            ],
            options={
                'db_table': 'SERVICE_',
            },
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('namectm', models.CharField(blank=True, max_length=15, null=True)),
                ('address_field', models.CharField(blank=True, max_length=50, null=True)),
                ('phone', models.CharField(blank=True, max_length=12, null=True)),
                ('Avatar', models.ImageField(default=True, upload_to='images')),
                ('idctm', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='members.registetuser')),
            ],
            options={
                'db_table': 'CUSTOMER',
            },
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ship_date', models.DateField()),
                ('ship_amount', models.IntegerField(blank=True, null=True)),
                ('idctm', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='members.customer')),
                ('idpd', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='members.product')),
            ],
            options={
                'db_table': 'ORDER_',
                'unique_together': {('idctm', 'idpd', 'ship_date')},
            },
        ),
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.IntegerField(blank=True, null=True)),
                ('idctm', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='members.customer')),
                ('idpd', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='members.product')),
            ],
            options={
                'db_table': 'CART',
                'unique_together': {('idctm', 'idpd')},
            },
        ),
        migrations.CreateModel(
            name='BookService',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book_date', models.DateTimeField()),
                ('idctm', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='members.customer')),
                ('idsv', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='members.service')),
            ],
            options={
                'db_table': 'BOOK_SERVICE',
                'unique_together': {('idctm', 'idsv', 'book_date')},
            },
        ),
    ]