# Generated by Django 5.1.2 on 2024-11-19 11:33

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Obat',
            fields=[
                ('idObat', models.AutoField(primary_key=True, serialize=False, verbose_name='ID Obat')),
                ('namaObat', models.CharField(max_length=100, verbose_name='Nama Obat')),
                ('harga', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Harga')),
                ('stok', models.IntegerField(verbose_name='Jumlah Stok')),
                ('deskripsi', models.TextField(blank=True, null=True, verbose_name='Deskripsi Obat')),
            ],
            options={
                'verbose_name': 'Obat',
                'verbose_name_plural': 'Obat-obatan',
            },
        ),
        migrations.CreateModel(
            name='Pelanggan',
            fields=[
                ('id_pelanggan', models.AutoField(primary_key=True, serialize=False, verbose_name='ID Pelanggan')),
                ('nama_pelanggan', models.CharField(max_length=100, verbose_name='Nama Pelanggan')),
                ('no_telepon', models.CharField(max_length=15, verbose_name='Nomor Telepon')),
                ('alamat', models.TextField(verbose_name='Alamat')),
                ('penyakit', models.CharField(max_length=100, verbose_name='Penyakit')),
                ('jenis_kelamin', models.CharField(choices=[('L', 'Laki-laki'), ('P', 'Perempuan')], max_length=10, verbose_name='Jenis Kelamin')),
                ('umur', models.IntegerField(verbose_name='Umur')),
            ],
            options={
                'verbose_name': 'Pelanggan',
                'verbose_name_plural': 'Pelanggan',
            },
        ),
        migrations.CreateModel(
            name='Supplier',
            fields=[
                ('id_supplier', models.AutoField(primary_key=True, serialize=False, verbose_name='ID Supplier')),
                ('nama_supplier', models.CharField(max_length=100, verbose_name='Nama Supplier')),
                ('alamat', models.TextField(verbose_name='Alamat')),
                ('no_telepon', models.CharField(max_length=15, verbose_name='Nomor Telepon')),
            ],
            options={
                'verbose_name': 'Supplier',
                'verbose_name_plural': 'Supplier',
            },
        ),
        migrations.CreateModel(
            name='Membeli',
            fields=[
                ('id_membeli', models.AutoField(primary_key=True, serialize=False, verbose_name='ID Pembelian')),
                ('tgl_pembelian', models.DateField(verbose_name='Tanggal Pembelian')),
                ('id_obat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pembayaran2.obat', verbose_name='Obat')),
                ('id_pelanggan', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pembayaran2.pelanggan', verbose_name='Pelanggan')),
            ],
            options={
                'verbose_name': 'Pembelian',
                'verbose_name_plural': 'Pembelian',
            },
        ),
        migrations.CreateModel(
            name='Memasok',
            fields=[
                ('id_memasok', models.AutoField(primary_key=True, serialize=False, verbose_name='ID Memasok')),
                ('obat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pembayaran2.obat', verbose_name='Obat')),
                ('supplier', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pembayaran2.supplier', verbose_name='Supplier')),
            ],
            options={
                'verbose_name': 'Memasok',
                'verbose_name_plural': 'Memasok',
            },
        ),
    ]
