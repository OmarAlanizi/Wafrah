from django.db import models

# Create your models here.
class Permission(models.Model):
    permission_name = models.TextField()

class Product(models.Model):
    product_name = models.TextField()
    product_amount = models.PositiveIntegerField()
    product_price = models.DecimalField(decimal_places=2, max_digits=6)

class Company(models.Model):
    company_name = models.TextField()

class Supplier(models.Model):
    supplier_name = models.TextField()
    products = models.ManyToManyField(Product)

class Order(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)
    products = models.ForeignKey(Product, on_delete=models.CASCADE)

class SupportTicket(models.Model):
    issue = models.TextField()

class Account(models.Model):
    email = models.EmailField()
    username = models.CharField(max_length=30)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    permissions = models.ManyToManyField(Permission)