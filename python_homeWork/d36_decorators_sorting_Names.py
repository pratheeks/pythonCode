import operator as op

def person_lister(f):
    def inner(people):
        people.sort(key=op.itemgetter(2))
        # print(people)
        # l=[]
        # for p in people:
        #     l.append(f(p))
        # return l
        return [f(p) for p in people]
        # return map(f,people)
        # return map(f, sorted(people, key=lambda x: int(x[2])))
        # complete the function
    return inner

@person_lister
def name_format(person):
    print(person)
    # for i in person:
    #     print(("Mr. " if i[3] == "M" else "Ms. ") + i[0] + " " + i[1])
    return ("Mr. " if person[3] == "M" else "Ms. ") + person[0] + " " + person[1]

if __name__ == '__main__':
    people = [input().split() for i in range(int(input()))]
    # print(people)
    # name_format(people)
    print(*name_format(people), sep='\n')