from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from .backends import *
from .forms import *
from .models import *
from .test_db import test



def home(request):
    context = {}
    if check_login_company(request):
        company = Company.objects.get(pk=request.session['company_id'])
        context = {
            'company':company,
            }
        return redirect('/retailer_dashboard')
    if check_login_supplier(request):
        supplier = Supplier.objects.get(pk=request.session['supplier_id'])
        context = {
            'supplier':supplier,
            }
        return redirect('/wholesaler_dashboard')
    # test()
    return render(request, 'index.html',context)
#company related forms, login and register
def login_page_company(request):
    if check_login_company(request):
        company = Company.objects.get(pk=request.session['company_id'])
        context = {
            'company':company,
            }
        print(company.company_name, company.company_email)
        return render(request, 'retailer_dashboard.html',context)

    form = CompanyLogin(request.POST or None)
    if form.is_valid():
        company_email  = form.cleaned_data.get("company_email")
        company_password  = form.cleaned_data.get("company_password")
        company = authenticate_company(request, username=company_email, password=company_password)
        if company is not None and not isinstance(company, str):
            request.session['company_id'] = company.pk
            print(request.session['company_id'])
            return redirect('/retailer_dashboard')
        else:
            if isinstance(company, str):
                form.add_error(field='company_email',error="Account doesn't exist!")
            else:
                form.add_error(field='company_email',error="Incorrect Email or password!")
            return render(request, 'login.html', {'form': form})

    return render(request, 'login.html', {'form': form})

def signup_company(request):
    if check_login_company(request):
        return render(request, 'retailer_dashboard.html')
    if request.method == 'POST':
        form = CompanySignUpForm(request.POST)
        if form.is_valid():
            print('valid')
            form.save()
            company_email  = form.cleaned_data.get("company_email")
            company_password  = form.cleaned_data.get("company_password")
            company = authenticate_company(request, username=company_email, password=company_password)
            request.session['company_id'] = company.pk
            print(request.session['company_id'])
            return login_page_company(request)
        else:
            print("not valid")
            return render(request, 'signup.html', {'form': form})

    form = CompanySignUpForm()
    return render(request, 'signup.html', {'form': form})       

#supplier related forms, login and register
def login_page_supplier(request):
    if check_login_supplier(request):
        supplier = Supplier.objects.get(pk=request.session['supplier_id'])
        context = {
            'supplier':supplier,
            }
        print(supplier.supplier_name, supplier.supplier_email)
        return render(request, 'wholesaler_dashboard.html',context)

    form = SupplierLogin(request.POST or None)
    if form.is_valid():
        supplier_email  = form.cleaned_data.get("supplier_email")
        supplier_password  = form.cleaned_data.get("supplier_password")
        supplier = authenticate_supplier(request, username=supplier_email, password=supplier_password)
        if supplier is not None and not isinstance(supplier, str):
            request.session['supplier_id'] = supplier.pk
            print(request.session['supplier_id'])
            return redirect('/wholesaler_dashboard')
        else:
            if isinstance(supplier, str):
                form.add_error(field='supplier_email',error="Account doesn't exist!")
            else:
                form.add_error(field='supplier_email',error="Incorrect Email or password!")
            return render(request, 'login.html', {'form': form})

    return render(request, 'login.html', {'form': form})

def signup_supplier(request):
    if check_login_supplier(request):
        return render(request, 'wholesaler_dashboard.html')
    if request.method == 'POST':
        form = SupplierSignUpForm(request.POST)
        if form.is_valid():
            print('valid')
            form.save()
            supplier_email  = form.cleaned_data.get("supplier_email")
            supplier_password  = form.cleaned_data.get("supplier_password")
            supplier = authenticate_supplier(request, username=supplier_email, password=supplier_password)
            request.session['supplier_id'] = supplier.pk
            print(request.session['supplier_id'])
            return login_page_supplier(request)
        else:
            print("not valid")
            return render(request, 'signup.html', {'form': form})

    form = SupplierSignUpForm()
    return render(request, 'signup.html', {'form': form})       

def logout(request):
    request.session.flush()
    return redirect('index')

def categories(request):
    return render(request, 'categories.html')

def manage_user(request):
    return render(request, 'manage_user.html')

def product_view(request):
    return render(request, 'product_view.html')

def retailer_dashboard(request):
    context = {}
    if check_login_company(request):
        company = Company.objects.get(pk=request.session['company_id'])
        orders = Order.objects.all().filter(company=company)
        context = {
            'company':company,
            'orders':orders,
            }
        
    return render(request, 'retailer_dashboard.html', context)

def wholesaler_dashboard(request):
    context = {}
    if check_login_supplier(request):
        supplier = Supplier.objects.get(pk=request.session['supplier_id'])
        orders = Order.objects.all().filter(supplier=supplier)
        context = {
            'supplier':supplier,
            'orders':orders,
            }
        
    return render(request, 'wholesaler_dashboard.html', context)

def add_product(request):
    if not check_login_supplier(request):
        return redirect('/')
    form = ProductForm()
    supplier = Supplier.objects.get(pk=request.session['supplier_id'])
    context = {
        'supplier':supplier,
        }

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product_name  = form.cleaned_data["product_name"]
            product_specs  = form.cleaned_data["product_specs"]
            # product_image  = form.cleaned_data["product_image"]
            product = SupplierProducts(
                product_name=product_name,
                product_specs=product_specs,
            )
            product.product_image = request.FILES["product_image"]
            # product = SupplierProducts.objects.create(
            #     product_name=product_name,
            #     product_specs=product_specs,
            #     product_image=product_image,
            # )
            product.save()
            return redirect('index')
    print("not valid")
    # image = SupplierProducts.objects.get(pk=5).product_image
    # print(image.url)
    print(request.FILES)
    return render(request, 'add_product.html', {'form': form})

    