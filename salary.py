employees={"Rajesh":50000,"vicky":75000,"Anvitha":80000}
high_salary=max(employees, key=employees.get)
print(f"highest salary holder :{high_salary} - {employees[high_salary]}")