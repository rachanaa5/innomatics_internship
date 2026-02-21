def filter_premium_crops(prices):
    premium = [p for p in prices if p > 2000] 
    print(f"Premium Crops: {premium}")

filter_premium_crops([1500, 2500, 1800, 3200])