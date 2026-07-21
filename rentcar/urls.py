from django.contrib import admin
from django.urls import path, include

admin.site.site_header = "Rental Mobil"
admin.site.site_title = "Rental Mobil"
admin.site.index_title = "Sistem Informasi Rental Mobil"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('pelanggan/', include('pelanggan.urls')),
]