from django.contrib import admin

# Register your models here.
from .models import MilkIndex
from .models import BrandInfo

admin.site.register(MilkIndex)
admin.site.register(BrandInfo)
