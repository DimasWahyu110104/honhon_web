from django.contrib import admin
from.models import pesanan

# Register your models here

class pesananAdmin(admin.ModelAdmin):
    list_display = ("tanggal", "pembeli","varian","jumlah_pesanan",)

admin.site.register(pesanan, pesananAdmin)
