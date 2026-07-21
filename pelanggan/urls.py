from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('mobil/', views.daftar_mobil, name='daftar_mobil'),
    path('sewa/', views.sewa_mobil, name='sewa_mobil'),
    path('riwayat/', views.riwayat_penyewaan, name='riwayat_penyewaan'),
]