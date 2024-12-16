from django.db import models
# Create your models here.
class Supplier(models.Model):
    id_supplier = models.AutoField(
        primary_key=True, 
        verbose_name="ID Supplier"
        )
    nama_supplier = models.CharField(
        max_length=100, 
        verbose_name="Nama Supplier"
        )
    alamat = models.TextField(
        verbose_name="Alamat")
    no_telepon = models.CharField(
        max_length=15, 
        verbose_name="Nomor Telepon")

    def __str__(self):
        return f"{self.id_supplier} - {self.nama_supplier}"

    class Meta:
        # Tidak menggunakan atribut ordering dan db_table
        verbose_name = "Supplier"
        verbose_name_plural = "Supplier"

class Obat(models.Model):
    idObat = models.AutoField(
        primary_key=True, 
        verbose_name="ID Obat"
    )
    namaObat = models.CharField(
        max_length=100, 
        verbose_name="Nama Obat"
    )
    harga = models.DecimalField(
        max_digits=10, 
        decimal_places=2, 
        verbose_name="Harga"
    )
    stok = models.IntegerField(
        verbose_name="Jumlah Stok"
    )
    deskripsi = models.TextField(
        blank=True, 
        null=True, 
        verbose_name="Deskripsi Obat"
    )

    def __str__(self):
        return f"{self.namaObat} - {self.deskripsi} - {self.harga}"

    class Meta:
        # Tidak menggunakan atribut ordering dan db_table
        verbose_name = "Obat"
        verbose_name_plural = "Obat-obatan"
    
class Memasok(models.Model):
    id_memasok = models.AutoField(
        primary_key=True, 
        verbose_name="ID Memasok")
    obat = models.ForeignKey(
        'Obat',  # Pastikan model Obat sudah didefinisikan
        on_delete=models.CASCADE,
        verbose_name="Obat"
    )
    supplier = models.ForeignKey(
        'Supplier',  # Pastikan model Supplier sudah didefinisikan
        on_delete=models.CASCADE,
        verbose_name="Supplier"
    )

    def __str__(self):
        return f"Memasok {self.id_memasok} - Obat: {self.obat} - Supplier: {self.supplier}"

    class Meta:
        # Tidak menggunakan atribut ordering dan db_table
        verbose_name = "Memasok"
        verbose_name_plural = "Memasok"

class DetailMemasok(models.Model):
    id = models.AutoField(verbose_name="idDetailPembelian", primary_key=True)
    idMemasok = models.ForeignKey(Memasok, verbose_name="idMembeli", on_delete=models.CASCADE)
    id_obat = models.ForeignKey(
        'Obat',  # Asumsikan ada model Obat yang sudah didefinisikan
        on_delete=models.CASCADE,
        verbose_name="Obat"
    )
    
    class Meta:
        verbose_name = "DetailPembelian"
        verbose_name_plural = "DetailPembelians"

    def __str__(self):
        return f'id: {self.id} - idMembeli: {self.idMembeli} - idObat: {self.id_obat}'

class Pelanggan(models.Model):
    id_pelanggan = models.AutoField(
        primary_key=True, 
        verbose_name="ID Pelanggan"
    )
    nama_pelanggan = models.CharField(
        max_length=100, 
        verbose_name="Nama Pelanggan"
    )
    no_telepon = models.CharField(
        max_length=15, 
        verbose_name="Nomor Telepon"
    )
    alamat = models.TextField(
        verbose_name="Alamat"
    )
    penyakit = models.CharField(
        max_length=100, 
        verbose_name="Penyakit"
    )
    jenis_kelamin = models.CharField(
        max_length=10,
        choices=[('L', 'Laki-laki'), ('P', 'Perempuan')],
        verbose_name="Jenis Kelamin"
    )
    umur = models.IntegerField(verbose_name="Umur")
    def __str__(self):
        return f"{self.id_pelanggan} - {self.nama_pelanggan}"

    class Meta:
        # Tidak menggunakan atribut ordering dan db_table
        verbose_name = "Pelanggan"
        verbose_name_plural = "Pelanggan"

class Membeli(models.Model):
    id_membeli = models.AutoField(
        primary_key=True, 
        verbose_name="ID Pembelian"
        )
    id_pelanggan = models.ForeignKey(
        'Pelanggan',  # Asumsikan ada model Pelanggan yang sudah didefinisikan
        on_delete=models.CASCADE,
        verbose_name="Pelanggan"
    )
    tgl_pembelian = models.DateField(verbose_name="Tanggal Pembelian")

    def __str__(self):
        return f"Pembelian {self.id_membeli} - {self.id_pelanggan}"

    class Meta:
        # Tidak menggunakan atribut ordering dan db_table
        verbose_name = "Pembelian"
        verbose_name_plural = "Pembelian"

class DetailPembelian(models.Model):
    id = models.AutoField(verbose_name="idDetailPembelian", primary_key=True)
    idMembeli = models.ForeignKey(Membeli, verbose_name="idMembeli", on_delete=models.CASCADE)
    id_obat = models.ForeignKey(
        'Obat',  # Asumsikan ada model Obat yang sudah didefinisikan
        on_delete=models.CASCADE,
        verbose_name="Obat"
    )
    
    class Meta:
        verbose_name = "DetailPembelian"
        verbose_name_plural = "DetailPembelians"

    def __str__(self):
        return f'id: {self.id} - idMembeli: {self.idMembeli} - idObat: {self.id_obat}'
    
    
