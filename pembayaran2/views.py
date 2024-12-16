from django.shortcuts import render
# from apotek.models import DetailPembelian
from django.db.models import Count

# Create your views here.
from pembayaran2.models import DetailPembelian, Memasok, Membeli, Pelanggan

def home(request):
    return render(request, 'home.html')

def tentang(request):
    return render(request, 'tentang.html')

def memesan(request):
    return render(request, 'memesan.html')

def kontak(request):
    return render(request, 'kontak.html')

def laporan_memasok(request):
    memasok_list = Memasok.objects.select_related('obat', 'supplier').all()
    return render(request, 'laporan_memasok.html', {'memasok_list': memasok_list})

def laporan_pembelian(request):
    # Query all purchases and their related data
    pembelian_list = Membeli.objects.select_related('id_pelanggan').all()

    laporan_data = []

    for pembelian in pembelian_list:
        # Get the details of the purchase (Obat, Harga)
        details = []
        for detail in DetailPembelian.objects.filter(idMembeli=pembelian):
            details.append({
                'nama_obat': detail.id_obat.namaObat,
                'harga': detail.id_obat.harga
            })

        laporan_data.append({
            'nama_pelanggan': pembelian.id_pelanggan.nama_pelanggan,
            'tgl_pembelian': pembelian.tgl_pembelian,
            'details': details
        })

    # Render the data in the template
    return render(request, 'laporan_pembelian.html', {'laporan_data': laporan_data})

def laporan_obat_terpopuler(request):
    # Query untuk mendapatkan obat terpopuler
    popular_obat = (
        DetailPembelian.objects.values('id_obat__namaObat')
        .annotate(jumlah_dibeli=Count('id_obat'))
        .order_by('-jumlah_dibeli')
    )
    
    # Kirim data ke template
    context = {
        'popular_obat': popular_obat
    }
    return render(request, 'laporan_obat_terpopuler.html', context)

def laporan_pembelian_pelanggan(request):
    # Query untuk mendapatkan data pembelian pelanggan
    laporan_pembelian = []
    for pembelian in Membeli.objects.select_related('id_pelanggan').all():
        detail_obat = DetailPembelian.objects.filter(idMembeli=pembelian)
        laporan_pembelian.append({
            'pelanggan': pembelian.id_pelanggan.nama_pelanggan,
            'tanggal_pembelian': pembelian.tgl_pembelian,
            'detail_obat': [{
                'nama_obat': detail.id_obat.namaObat,
                'harga': detail.id_obat.harga,
            } for detail in detail_obat]
        })

    # Kirim data ke template
    context = {
        'laporan_pembelian': laporan_pembelian
    }
    return render(request, 'laporan_pembelian_pelanggan.html', context)

def laporan_pelanggan_penyakit(request, penyakit):
    # Query untuk mendapatkan pelanggan berdasarkan penyakit
    pelanggan_list = []
    for pelanggan in Pelanggan.objects.filter(penyakit__icontains=penyakit):
        pembelian_list = []
        for pembelian in Membeli.objects.filter(id_pelanggan=pelanggan):
            detail_obat = DetailPembelian.objects.filter(idMembeli=pembelian)
            pembelian_list.append({
                'tanggal_pembelian': pembelian.tgl_pembelian,
                'detail_obat': [{
                    'nama_obat': detail.id_obat.namaObat,
                    'harga': detail.id_obat.harga,
                } for detail in detail_obat]
            })
        pelanggan_list.append({
            'nama_pelanggan': pelanggan.nama_pelanggan,
            'alamat': pelanggan.alamat,
            'pembelian_list': pembelian_list,
        })
    
    # Kirim data ke template
    context = {
        'penyakit': penyakit,
        'pelanggan_list': pelanggan_list,
    }
    return render(request, 'laporan_pelanggan_penyakit.html', context)