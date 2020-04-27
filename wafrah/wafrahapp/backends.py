from .models import Company, Supplier


def authenticate_company(self, username=None, password=None, **kwargs):
    try:
        company_obj = Company.objects.get(company_email=username)
        if company_obj.check_password(password):
            return company_obj
    except Company.DoesNotExist:
        return "Account doesn't exist!"
    return None

def check_login_company(request):
    try:
        request.session['company_id']
        return True
    except KeyError:
        return False

def authenticate_supplier(self, username=None, password=None, **kwargs):
    try:
        supplier_obj = Supplier.objects.get(supplier_email=username)
        if supplier_obj.check_password(password):
            return supplier_obj
    except Supplier.DoesNotExist:
        return "Account doesn't exist!"
    return None

def check_login_supplier(request):
    try:
        request.session['supplier_id']
        return True
    except KeyError:
        return False