from django.contrib import admin
# Register your models here.
from django import forms
from django.utils.html import mark_safe
from .models import *
from ckeditor_uploader.widgets import CKEditorUploadingWidget


class ProductForm(forms.ModelForm):
    descript=forms.CharField(widget=CKEditorUploadingWidget)

    class Meta:
        model=Product
        fields= '__all__'



class ProductAdmin(admin.ModelAdmin):
    
    list_display=["namepd","typepd","price"]
    search_fields=["namepd","typepd"]
    list_filter=["typepd"]
    readonly_fields=["imagepd"]
    form =ProductForm
    def imagepd(self,Product):
        return mark_safe(" <img src='/static/{img_url}'".format(img_url=Product.imgpd))

admin.site.register(Product,ProductAdmin)
admin.site.register(Order)
admin.site.register(BookService)
admin.site.register(Service)
admin.site.register(Cart)
admin.site.register(Customer)
admin.site.register(RegistetUser)
admin.site.site_header=" Motortoy System"