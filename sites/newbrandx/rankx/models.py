from django.db import models

class MilkIndex(models.Model):
    brand_name = models.CharField(max_length=200)
    index = models.IntegerField(default=0)
    pv = models.IntegerField(default=0)
    sales = models.IntegerField(default=0)
    pub_date = models.DateTimeField('date published')


class BrandInfo(models.Model):
    brand_name = models.CharField(max_length=200)
    country = models.CharField(max_length=200)
    startup = models.DateTimeField('company founded')
    scale = models.IntegerField(default=0)
    desc = models.CharField(max_length=2000)



