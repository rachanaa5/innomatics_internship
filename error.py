logs=["INFO","ERROR","WARNING","INFO","ERROR"]
error_count=0
for entry in logs:
    if entry=="ERROR":
        error_count+=1
print(f"total error :{error_count}")