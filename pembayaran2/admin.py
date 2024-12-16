from django.contrib import admin
from .models import Supplier,Obat,Memasok,Pelanggan,Membeli, DetailPembelian, DetailMemasok

# Register your models here.
admin.site.register(Supplier)
admin.site.register(Obat)
admin.site.register(Memasok)
admin.site.register(Pelanggan)
admin.site.register(Membeli)
admin.site.register(DetailPembelian)
admin.site.register(DetailMemasok)