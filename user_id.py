id=["id110", "id111", "id765", "id0987"]
counts={}
for vid in id:
    counts[uid]=counts.get(uid,0)+1
for uid, countt in counts.items():
    if countt >1:
        print(f"{uid}->{countt} times")