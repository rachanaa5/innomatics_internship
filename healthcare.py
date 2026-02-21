def monitor_stock(stock_lvl):
    if stock_lvl<10:
        status="Low Stock Alert"
    else:
        status="Stock Sufficient"
    print(f"Medicine Stock: {stock_lvl}")
    print(f"Status: {status}")

monitor_stock(6)