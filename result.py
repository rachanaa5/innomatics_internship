marks=[45,78,90,33,60,86,55]
pass_count=0
fail_count=0
for mark in marks:
    if mark>=50:
        pass_count+=1
    else:
        fail_count+=1
print("No.of students passed:", pass_count)
print("No.of students failed:", fail_count)