from django.contrib import admin

# Register your models here.
from .models import Milk
from .models import Brand
from .models import Company

admin.site.register(Milk)
admin.site.register(Brand)
admin.site.register(Company)

