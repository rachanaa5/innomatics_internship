emails=["name123@gmail.com","user@gmail.com","company@gmail.com","intern@gmail.com"]
domain_counts={}
for email in emails:
    domain=email.split('@')[1]
    domain_counts[domain]=domain_counts.get(domai,0)+1
    total_users =len(emails)
    for domain,count in domain_counts.items():
        percentage=(count/total_user)*100
        print(f"count in domain_counts")
