from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

#Perms not implemented yet
class Permission(models.Model):
    permission_name = models.TextField()

class SupplierProducts(models.Model):
    product_name = models.CharField(max_length=256)
    product_specs = models.CharField(max_length=256)
    product_image = models.ImageField(verbose_name='product_image',upload_to='products/', default = 'pic_folder/None/no-img.jpg', null=True, blank=True)

class Product(models.Model):
    product_name = models.ForeignKey(SupplierProducts, on_delete=models.DO_NOTHING)
    product_amount = models.TextField()
    product_price = models.DecimalField(decimal_places=2, max_digits=6)

class CompanyManager(BaseUserManager):
    def create_company(self, company_name, company_email, company_password):
        if not company_email:
            raise ValueError("Company must have E-Mail address.")
        company_obj = self.model(
            company_email = self.normalize_email(company_email),
        )
        company_obj.set_password(company_password)
        company_obj.company_name = company_name
        company_obj.save(using=self._db)
        return company_obj

class Company(AbstractBaseUser):
    company_name = models.CharField(max_length=256, unique=True)
    company_email = models.EmailField(unique=True)

    USERNAME_FIELD = 'company_email'
    REQUIRED_FIELDS = ['company_name', 'company_email', 'company_password']

    objects = CompanyManager()

    def __str__(self):
        return self.company_name

class SupplierManager(BaseUserManager):
    def create_supplier(self, supplier_name, supplier_email, supplier_password):
        if not supplier_email:
            raise ValueError("supplier must have E-Mail address.")
        supplier_obj = self.model(
            supplier_email = self.normalize_email(supplier_email),
        )
        supplier_obj.set_password(supplier_password)
        supplier_obj.supplier_name = supplier_name
        supplier_obj.save(using=self._db)
        return supplier_obj

class Supplier(AbstractBaseUser):
    supplier_name = models.CharField(max_length=256, unique=True)
    supplier_email = models.EmailField(unique=True)
    products = models.ManyToManyField(SupplierProducts)

    USERNAME_FIELD = 'supplier_email'
    REQUIRED_FIELDS = ['supplier_name', 'supplier_email', 'supplier_password']

    objects = SupplierManager()

    def __str__(self):
        return self.supplier_name

#Accs not implemented yet
class Account(models.Model):
    email = models.EmailField()
    username = models.CharField(max_length=30)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    permissions = models.ManyToManyField(Permission)

class Order(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product)
    status = models.TextField(default='Sent')
    created = models.DateTimeField(auto_now_add=True)
    # order_by = models.ForeignKey(Account, on_delete=models.DO_NOTHING)

class SupportTicket(models.Model):
    issue = models.TextField()


