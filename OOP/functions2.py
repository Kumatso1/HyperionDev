def purchase_product(product_type, price, mobile_brand = None):
    delivery_charge=40
    if product_type == "Mobile":
        if mobile_brand == "Apple":
            discount = 10
            delivery_charge=0
        else:
            discount = 50
        total_price = price - price * discount / 100
    else:
        total_price = price + price * 2 / 100 + delivery_charge

    print(f"Total price of {product_type} is {total_price}")

purchase_product("Mobile", 20000, "Apple")
purchase_product("Shoe", 350)

# This is the upgraded version of the above program 
print("\n The upgraded program of the above is give below")

def purchase_product(product_type,price,mobile_brand,material):
    delivery_charge=40
    if product_type == "Mobile":
        if mobile_brand == "Apple":
            discount = 10
            delivery_charge=0
        else:
            delivery_charge=50
            discount = 5
        total_price = price + delivery_charge- price * discount / 100
    else:
        if material == "leather":
            tax = 5
        else:
            tax = 2
        total_price = price +delivery_charge+ price * tax / 100
    print("Total price of "+product_type+" is "+str(total_price))

purchase_product("Mobile",20000,"Apple",None)
purchase_product("Shoe",350,None,"leather")
                                                    