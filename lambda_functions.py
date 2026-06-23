names = input("enter names ").split(",")
filtered_names = filter(lambda name: 'a' in name.lower(), names)
for name in filtered_names:
    print(name)
