phoneBook = {}
n = int(input())


for _ in range(n):
    contact = input()
    name, phone = contact.split()
    phoneBook[name] = phone
    


try:
    while True:
        name = input()
        if name in phoneBook:
            print(f"{name}={phoneBook[name]}")
        else:
            print("Not found")
except EOFError:
    pass
