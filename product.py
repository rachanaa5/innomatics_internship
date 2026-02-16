costs=[680,975,450,120,876,8760,1200]
total=sum(1 for c in costs if c>1000)
print(f"products above 1000:{total}")