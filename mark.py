def process_result(marks):
    total=0
    for m in marks:
        total +=m
        avg = total/len(marks)
        if avg >=50:
            print(f"Average:{avg.2f}-status:Passed")
        else:
            print(f"average:{avg.2f}-status:Failed")

marks=[45,65,78,34,56]
print(process_result(marks))