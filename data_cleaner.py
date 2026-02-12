names=["Alice","bob","CHRLIE"]
correct_names=[]
for name in names:
    corrected_names= name.strip().lower()
    correct_names.append(corrected_names)
print(correct_names)