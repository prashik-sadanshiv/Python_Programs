

data = [
    int(input("Enter integer: ")),
    input("Enter string "),
    float(input("Enter float: ")),
    input("Enter Boolean (true/false): ").split().lower() == "true"
]

print(data)
print([type(item) for item in data])