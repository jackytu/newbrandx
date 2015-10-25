from django.db import models

class Company(models.Model):
    name = models.CharField(max_length=200)
    country = models.CharField(max_length=200)
    website = models.CharField(max_length=400)
    startup = models.DateField('company founded')
    scale = models.IntegerField(default=0)
    desc = models.CharField(max_length=2000)

    class Meta:
        verbose_name = 'Company'
        verbose_name_plural = 'Company'

    def __unicode__(self):
        return self.name

class Brand(models.Model):
    name = models.CharField(max_length=200)
    company = models.ForeignKey(Company, related_name = 'company_name')

    class Meta:
        verbose_name = 'Brand'
        verbose_name_plural = 'Brand'

    def __unicode__(self):
        return self.name

class Milk(models.Model):
    brand_record = models.CharField(max_length=200)
    brand_name = models.ForeignKey(Brand, related_name = 'brand_name')
    rank = models.IntegerField(default=0)
    pv = models.IntegerField(default=0)
    taobao_sales = models.IntegerField(default=0)
    jd_sales = models.IntegerField(default=0)
    tmall_sales = models.IntegerField(default=0)
    vip_sales = models.IntegerField(default=0)
    amazon_sales = models.IntegerField(default=0)
    weibo_fans = models.IntegerField(default=0)
    weibo_forward = models.IntegerField(default=0)
    weixin_fans = models.IntegerField(default=0)
    pub_date = models.DateField('date published')

    class Meta:
        verbose_name = 'Milk'
        verbose_name_plural = 'Milk'

    def __unicode__(self):
        return self.brand_record


