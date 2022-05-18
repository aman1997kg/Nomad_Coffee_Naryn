from django.contrib import admin
from .models import *

#class CatMenuAdmin(admin.ModelAdmin):
   # prepopulated_fields = {"slug": ("cat_menu_name",)}

#class BaseMenuAdmin(admin.ModelAdmin):
   # prepopulated_fields = {"slug": ("title_menu",)}


admin.site.register(CatMenu)
admin.site.register(BaseMenu)

