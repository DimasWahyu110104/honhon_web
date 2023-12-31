from django.db import models

# Create your models here.

class pesanan(models.Model):
    tanggal = models.CharField(max_length=50)
    pembeli = models.CharField(max_length=50)
    varian = models.CharField(max_length=50)
    jumlah_pesanan = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.tanggal}"

