from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from administrator.models import Mobil, Penyewaan
from datetime import datetime

@login_required
def dashboard(request):
    return render(request, 'pelanggan/dashboard.html')

@login_required
def redirect_user(request):
    user = request.user

    if user.role == 'administrator':
        return redirect('/administrator/')
    elif user.role == 'petugas':
        return redirect('/petugas/')
    elif user.role == 'pelanggan':
        return redirect('/pelanggan/')

    return redirect('/admin/')

def daftar_mobil(request):
    mobils = Mobil.objects.all()
    return render(request, 'pelanggan/daftar_mobil.html', {'mobils': mobils})

def sewa_mobil(request):
    mobils = Mobil.objects.filter(tersedia=True)

    if request.method == 'POST':
        mobil_id = request.POST.get('mobil')
        tanggal_sewa = request.POST.get('tanggal_sewa')
        tanggal_kembali = request.POST.get('tanggal_kembali')

        mobil = Mobil.objects.get(id=mobil_id)

        tgl_sewa = datetime.strptime(tanggal_sewa, '%Y-%m-%d')
        tgl_kembali = datetime.strptime(tanggal_kembali, '%Y-%m-%d')

        lama_sewa = (tgl_kembali - tgl_sewa).days

        if lama_sewa <= 0:
            lama_sewa = 1

        total_biaya = lama_sewa * mobil.harga_harian

        Penyewaan.objects.create(
            pelanggan=request.user,
            mobil=mobil,
            tanggal_sewa=tanggal_sewa,
            tanggal_kembali=tanggal_kembali,
            lama_sewa=lama_sewa,
            total_biaya=total_biaya,
            dengan_supir=False,
            metode_pembayaran='Transfer',
            status='diajukan'
        )

        return render(request, 'pelanggan/sukses.html', {
            'mobil': mobil,
            'lama_sewa': lama_sewa,
            'total_biaya': total_biaya
        })

    return render(request, 'pelanggan/sewa_mobil.html', {'mobils': mobils})
def riwayat_penyewaan(request):
    penyewaans = Penyewaan.objects.filter(
        pelanggan=request.user
    ).order_by('-tanggal_sewa')

    return render(
        request,
        'pelanggan/riwayat_penyewaan.html',
        {'penyewaans': penyewaans}
    )