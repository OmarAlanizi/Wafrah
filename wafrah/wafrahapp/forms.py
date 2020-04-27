from django import forms
from .models import Company, Supplier, SupplierProducts


class CompanySignUpForm(forms.ModelForm):
    company_name = forms.CharField(widget=forms.TextInput(attrs={'class':'inputs','type':'text'}))
    company_email = forms.CharField(widget=forms.TextInput(attrs={'class':'inputs','type':'email'}))
    company_password = forms.CharField(widget=forms.TextInput(attrs={'class':'inputs','type':'password'}))
    verify_password = forms.CharField(widget=forms.TextInput(attrs={'class':'inputs','type':'password'}))

    class Meta:
        model = Company
        fields = ('company_name', 'company_email', 'company_password')

    def clean_verify_password(self):
        password1 = self.cleaned_data.get("company_password")
        password2 = self.cleaned_data.get("verify_password")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords do not match.")
        return password2
    def save(self, commit=True):
        company_obj = super(CompanySignUpForm, self).save(commit=False)
        company_obj.set_password(self.cleaned_data['company_password'])
        if commit:
            company_obj.save()
        return company_obj


class CompanyLogin(forms.Form):
    company_email = forms.EmailField(widget=forms.TextInput(attrs={'class':'inputs','type':'email'}))
    company_password = forms.CharField(widget=forms.TextInput(attrs={'class':'inputs','type':'password'}))


class SupplierSignUpForm(forms.ModelForm):
    supplier_name = forms.CharField(widget=forms.TextInput(attrs={'class':'inputs','type':'text'}))
    supplier_email = forms.CharField(widget=forms.TextInput(attrs={'class':'inputs','type':'email'}))
    supplier_password = forms.CharField(widget=forms.TextInput(attrs={'class':'inputs','type':'password'}))
    verify_password = forms.CharField(widget=forms.TextInput(attrs={'class':'inputs','type':'password'}))

    class Meta:
        model = Supplier
        fields = ('supplier_name', 'supplier_email', 'supplier_password')

    def clean_verify_password(self):
        password1 = self.cleaned_data.get("supplier_password")
        password2 = self.cleaned_data.get("verify_password")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords do not match.")
        return password2
    def save(self, commit=True):
        supplier_obj = super(SupplierSignUpForm, self).save(commit=False)
        supplier_obj.set_password(self.cleaned_data['supplier_password'])
        if commit:
            supplier_obj.save()
        return supplier_obj


class SupplierLogin(forms.Form):
    supplier_email = forms.EmailField(widget=forms.TextInput(attrs={'class':'inputs','type':'email'}))
    supplier_password = forms.CharField(widget=forms.TextInput(attrs={'class':'inputs','type':'password'}))

class ProductForm(forms.Form):
    product_name = forms.CharField(widget=forms.Textarea(attrs={'class':'text-area', 'placeholder':'Product name'}))
    product_specs = forms.CharField(widget=forms.Textarea(attrs={'class':'text-area', 'placeholder':'Product description'}))
    product_image = forms.ImageField()
    
    class Meta:
        model = SupplierProducts
        fields = ('product_name', 'product_specs', 'product_image')
    # def __init__(self, *args, **kwargs):
    #     super(ProductForm, self).__init__(*args, **kwargs)
    #     self.fields['product_image'].required = False