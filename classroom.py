def monitor_resources(usage_dict):
    overused = [res for res, hours in usage_dict.items() if hours > 8]
    alert = "Yes" if overused else "No"
    print(f"Overused Resources: {', '.join(overused) if overused else 'None'}")
    print(f"Energy Alert: {alert}")
monitor_resources({"Projector": 6, "AC": 9, "Lights": 4})