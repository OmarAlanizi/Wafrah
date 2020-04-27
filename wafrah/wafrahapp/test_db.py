from .models import *

def test():
    product1 = Product(
        product_name="Coffee",
        product_amount="100 Kilograms",
        product_price=100.5)
    product1.save()

    product2 = Product(
        product_name="Milk",
        product_amount="10 Litres",
        product_price=99.32)
    product2.save()
    
    product3 = Product(
        product_name="Plastic Straws",
        product_amount="100 Pieces",
        product_price=20)
    product3.save()

    company = Company.objects.get(company_name="test")
    # supplier = Supplier(
    #     supplier_name="Test inc.",
    # )
    # supplier.save()
    supplier = Supplier.objects.get(supplier_name="ses")
    supplier.products.add(product1)
    supplier.products.add(product2)
    supplier.products.add(product3)


    order1 = Order(
        company=company,
        supplier=supplier,
        status="Sent",
    )
    order1.save()
    order1.products.add(product1)
    order1.products.add(product2)

    # order1.save()
    print(order1)