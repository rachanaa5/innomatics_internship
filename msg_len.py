msg=["hi","welcome to platform","ok"]
for msgs in msg:
    lenght=len(msgs)
    status=""
    if lenght>10:
        status="long msg flagged"
    print(f"length:{lenght}, status:{status}")