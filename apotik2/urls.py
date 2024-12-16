"""
URL configuration for apotik2 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from pembayaran2.views import (
    home,
    tentang,
    memesan,
    kontak,
    laporan_memasok,
    laporan_pembelian_pelanggan,
    laporan_pembelian,
    laporan_pelanggan_penyakit,
    laporan_obat_terpopuler,
)  # Import semua views

urlpatterns = [
    # Admin site
    path('admin/', admin.site.urls),

    # Halaman utama
    path('', home, name='home'),
    path('tentang/', tentang, name='tentang'),
    path('memesan/', memesan, name='memesan'),
    path('kontak/', kontak, name='kontak'),

    # Laporan
    path('laporan/memasok/', laporan_memasok, name='laporan_memasok'),
    path('laporan/pembelian-pelanggan/', laporan_pembelian_pelanggan, name='laporan_pembelian_pelanggan'),
    path('laporan-pembelian/', laporan_pembelian, name='laporan_pembelian'),
    path('laporan/pelanggan-penyakit/<str:penyakit>/', laporan_pelanggan_penyakit, name='laporan_pelanggan_penyakit'),
    # path('laporan/obat-terpopuler/', laporan_obat_terpopuler, name='laporan_obat_terpopuler'),
    path('laporan/obat-terpopuler/', laporan_obat_terpopuler, name='laporan_obat_terpopuler'),

]
