import enum
class country(enum.IntEnum):
    Afghanistan = 93
    Albania = 355
    Algeria = 213
    Andorra = 376
    Angola = 244
    Antarctica = 672

print("\n".join(' '+c.name for c in sorted(country)))

print('-------------------------------------------------')

for c in sorted(country):
    print(''.join(' '+c.name))
    print(c.name)

print("---------------------------------------------------")

code_list=list(map(str, country))
print(code_list)

code_list=list(map(int, country))
print(code_list)