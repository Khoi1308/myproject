
from django.db import models
from ckeditor.fields import RichTextField
class RegistetUser(models.Model):
    class Meta:
        db_table = 'RegistetUser'
    username=models.CharField( max_length=100,  blank=True, null=True)
    email=models.CharField( max_length=100,  blank=True, null=True)
    password=models.CharField( max_length=100,  blank=True, null=True)

class Customer(models.Model):
    class Meta:
        db_table = 'CUSTOMER'
    idctm = models.ForeignKey(RegistetUser,on_delete=models.CASCADE )  # Field name made lowercase.
    namectm = models.CharField( max_length=15, blank=True, null=True)  # Field name made lowercase.
    address_field = models.CharField(max_length=50, blank=True, null=True)  # Field name made lowercase. Field renamed because it ended with '_'.
    phone = models.CharField( max_length=12,  blank=True, null=True)  # Field name made lowercase.
    Avatar= models.ImageField( upload_to="images",default=True)
   

class Service(models.Model):
    class Meta:
        db_table = 'SERVICE_'
    idsv = models.CharField(primary_key=True, max_length=3)  # Field name made lowercase.
    namesv = models.CharField( max_length=40,  blank=True, null=True)  # Field name made lowercase.
    price = models.CharField( max_length=10,  blank=True, null=True)  # Field name made lowercase.


class BookService(models.Model):
    class Meta:
        db_table = 'BOOK_SERVICE'
        unique_together = (('idctm', 'idsv', 'book_date'),)
    idctm = models.ForeignKey(Customer,on_delete=models.CASCADE)  # Field name made lowercase.
    idsv = models.ForeignKey(Service, on_delete=models.CASCADE)  # Field name made lowercase.
    book_date = models.DateTimeField()  # Field name made lowercase.


class Product(models.Model):
    class Meta:
        db_table = 'PRODUCT'
    idpd = models.CharField( primary_key=True, max_length=5)  # Field name made lowercase.
    namepd = models.CharField( max_length=1000, blank=True, null=True)  # Field name made lowercase.
    typepd = models.CharField( max_length=30, blank=True, null=True)  # Field name made lowercase.
    price = models.CharField( max_length=15, blank=True, null=True)  # Field name made lowercase.
    amount = models.IntegerField( blank=True, null=True)  # Field name made lowercase.
    branch = models.CharField( max_length=40, blank=True, null=True)  # Field name made lowercase.
    descript = RichTextField(blank=True, null=True)  # Field name made lowercase.
    imgpd = models.ImageField( upload_to="images",default=True)  # Field name made lowercase.


class Cart(models.Model):
    class Meta:
        db_table = 'CART'
        unique_together = (('idctm', 'idpd'),)
    idctm = models.ForeignKey(Customer, on_delete=models.CASCADE)  # Field name made lowercase.
    idpd = models.ForeignKey(Product,on_delete=models.CASCADE)  # Field name made lowercase.
    amount = models.IntegerField( blank=True, null=True)  # Field name made lowercase.

class Order(models.Model):
    class Meta:
        db_table = 'ORDER_'
        unique_together = (('idctm', 'idpd', 'ship_date'),)
    idctm = models.ForeignKey(Customer,on_delete=models.DO_NOTHING)  # Field name made lowercase.
    idpd = models.ForeignKey(Product, on_delete=models.DO_NOTHING)  # Field name made lowercase.
    ship_date = models.DateField()  # Field name made lowercase.
    ship_amount = models.IntegerField( blank=True, null=True)  # Field name made lowercase.

