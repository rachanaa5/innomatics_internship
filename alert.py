def check_inv(stock_data):
    for product, quantity in stock_data.items():
        if quantity <15:
            print(f"Alert:{product}stock is low({quantity}.)")
        else:
            print(f"Status:{producr}is stocked({quantity})")

inventory= {"product1":10,"product2":98,"product3":56,"product4":2}
check_inv(inventory)