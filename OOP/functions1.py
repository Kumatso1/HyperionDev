def purchase_product(product_type, price):
    discount=10
    delivery_charge=40
    if (price >= 500):
        discount=20
        delivery_charge=0
    else:
        discount=10
        delivery_charge=40
    total_price=price+delivery_charge-(price*discount/100)
    print(f"Total price of {product_type} is {total_price}")
purchase_product("Mobile",20000)
purchase_product("Shoe",350)