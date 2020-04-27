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

    company = Company.objects.get(company_name="test")
    # supplier = Supplier(
    #     supplier_name="Test inc.",
    # )
    # supplier.save()
    supplier = Supplier.objects.get(supplier_name="ses")
    supplier.products.add(product1)
    supplier.products.add(product2)

    test_acc = Account(
        email="test_email@test.com",
        username="test_acc",
        company=company,
    )
    test_acc.save()

    order1 = Order(
        company=company,
        supplier=supplier,
        status="Sent",
        order_by=test_acc
    )
    order1.save()
    order1.products.add(product1)
    order1.products.add(product2)

    # order1.save()
    print(order1)