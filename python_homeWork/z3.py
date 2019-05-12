def reverse(names):
    namesplit = names.split()
    s = " "
    print(s.join(namesplit[::-1]))

full_name = input("Enter your full name: ")
reverse(full_name)