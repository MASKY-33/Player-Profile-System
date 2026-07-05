choice = input("What do you want? (1 = Write, 2 = Read, 3 = Reset): ")


if choice == "1":
    write = input("Type your notition: ")
    with open("notition.txt", "a") as file:
        file.write(f"{write} \n")


elif choice == "2":
    with open("notition.txt", "r") as file:
        content = file.read()

    print(content)


elif choice == "3":
    with open("notition.txt", "w") as file:
        file.write("")