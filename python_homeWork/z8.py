from collections import defaultdict
classes=(
    ('V', 1),
    ('VI', 1),
    ('V', 2),
    ('VI', 2),
    ('VI', 3),
    ('VII', 1),
)
class_rollno=defaultdict(list)

for class_name, roll_id in classes:
    class_rollno[class_name].append(roll_id)
print(class_rollno)

from collections import Counter
students=Counter(class_name for class_name, no_students in classes)
print(students)

