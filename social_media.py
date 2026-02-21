def analyze_engagement(likes):
    total_likes=sum(likes)
    status="Viral Post"if total_likes>=1000 else "Normal Engagement"
    print(f"Total Likes:{total_likes}")
    print(f"Post Status:{status}")

analyze_engagement([400, 300, 350])