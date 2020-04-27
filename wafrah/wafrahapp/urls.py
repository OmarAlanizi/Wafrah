from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name='index'),
    path('company/login', views.login_page_company, name='company/login'),
    path('company/signup', views.signup_company, name='company/signup'),
    path('supplier/login', views.login_page_supplier, name='supplier/login'),
    path('supplier/signup', views.signup_supplier, name='supplier/signup'),
    path('logout', views.logout, name='logout'),
    path('categories', views.categories, name='categories'),
    path('manage_user', views.manage_user, name='manage_user'),
    path('product_view', views.product_view, name='product_view'),
    path('retailer_dashboard', views.retailer_dashboard, name='retailer_dashboard'),
    path('wholesaler_dashboard', views.wholesaler_dashboard, name='wholesaler_dashboard'),
    path('add_product', views.add_product, name='add_product'),
] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
