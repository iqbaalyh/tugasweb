from django.db import models  
class Service(models.Model):  
    sid = models.CharField(max_length=20)  
    sname = models.CharField(max_length=100)    
    scontact = models.CharField(max_length=15)
    sdeksripsi_keluhan = models.CharField(max_length=100)  
    class Meta:  
        db_table = "service"  