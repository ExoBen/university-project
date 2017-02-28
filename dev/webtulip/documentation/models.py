from django.db import models

# Create your models here.


class Network(models.Model):
    TLP_TYPE = "tlp"
    IND_TYPE = "ind"
    NET_CHOICES = [
        (TLP_TYPE, 'Tulip TLP'),
        (IND_TYPE, 'Industry Standard')
    ]

    network_name = models.CharField(max_length=255, blank=True, verbose_name="Network Name", unique=True)
    network_file = models.FileField(upload_to='networks/', verbose_name="Network File")
    network_type = models.CharField(max_length=3, choices=NET_CHOICES, default=TLP_TYPE, verbose_name="Network Type")
    uploaded_at = models.DateTimeField(auto_now_add=True)


