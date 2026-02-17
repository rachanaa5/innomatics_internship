employee={"Ram":87,"Amith":98,"Kumar":77,"Kiran":92}
max_score=max(employee.values())
top_performer=[name for name , score in employee.items() if score==max_score]
print(f"Top performers eligible for bonus are:{','.join(top_performer)}(score:{max_score})")
