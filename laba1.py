groupmates = [
    {
        "name": "Александр",
        "surname": "Иванов",
        "exams": ["Информатика", "ЭЭиС", "Web"],
        "marks": [4, 3, 5]
    },
    {
        "name": "Иван",
        "surname": "Петров",
        "exams": ["История", "АиГ", "КТП"],
        "marks": [4, 4, 4]
    },
    {
        "name": "Кирилл",
        "surname": "Смирнов",
        "exams": ["Философия", "ИС", "КТП"],
        "marks": [5, 5, 3]
    },
    {
        "name": "Владимир",
        "surname": "Суворов",
        "exams": ["Информатика", "ЭЭиС", "Web"],
        "marks": [5, 5, 5]
    },
    {
        "name": "Виктор",
        "surname": "Редискин",
        "exams": ["История", "АиГ", "КТП"],
        "marks": [3, 3, 3]
    },
    {
        "name": "Марк",
        "surname": "Родионов",
        "exams": ["Философия", "ИС", "КТП"],
        "marks": [5, 4, 5]
    }
]

def print_students(students):
    print(u"Имя".ljust(15), u"Фамилия".ljust(10), u"Экзамены".ljust(30), u"Оценки".ljust(20))
    for student in students:
        print(student["name"].ljust(15), student["surname"].ljust(10), str(student["exams"]).ljust(30), str(student["marks"]).ljust(20))


def sort_students(students):
    average_score=input()
    mem=[]
    for student in students:
        temp=0
        for i in range(3):
            temp=student["marks"][i]+temp
        temp=temp/3
        if temp<float(average_score):
            mem.append(student)
    for j in range(len(mem)):
        students.remove(mem[j])

print(type(groupmates))
sort_students(groupmates)
print_students(groupmates)
