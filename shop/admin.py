from django.contrib import admin
from.models import*

# Register your models here.
class categadmin(admin.ModelAdmin):
    prepopulated_fields={'slug':('name',)}
    list_display=['slug']
admin.site.register(categ,categadmin)


class prodAdmin(admin.ModelAdmin):
    prepopulated_fields={'slug':('name',)}
    list_display=['name','slug','price','stock','img','available','category']
    list_editable=['price','stock','img','available','category']
admin.site.register(products,prodAdmin)

