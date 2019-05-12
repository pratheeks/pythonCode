from enum  import Enum
class Country(Enum):
    Afghanistan = 93
    Albania = 355
    Algeria = 213
    Andorra = 376
    Angola = 244
    Antarctica = 672
print('\nMember name: {}'.format(Country.Albania.name))
print('Member value: {}'.format(Country.Albania.value))

print("-------------------------------------------------------")

for data in Country:
    print("Member name: {:15}".format(data.name))
    print("Member value: {}".format(data.value))

print("-------------------------------------------------------")

for data in Country:
    print("{:15} : {}".format(data.name, data.value))

print("-------------------------------------------------------")

for c in Country:
    print(''.join(' '+c.name))
    print(' '.join('  '+c.name))
    print(c)
print("-------------------------------------------------------")

print(Country.Albania.name)
print(Country.Albania)
print(Country)

