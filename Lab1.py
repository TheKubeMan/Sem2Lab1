def studentSort (students, score):
    newStudentList = []
    for i in range(0, len(students)):
        if students[i][3] > score:
            newStudentList.insert(len(newStudentList), students[i])
    printStudents(newStudentList)

def printStudents(students):
    for i in range(0, len(students)):
        print(students[i][0] + " " + students[i][1] + ", " + students[i][2] + " - " + str(students[i][3]))

stud = [
    ["Дмитрий", "Кубатин", "ВвИТ", 80], 
    ["Иван", "Плотников", "Философия", 40], 
    ["Василий", "Длинноногий", "Высшая математика", 78], 
    ["Владимир", "Ясный", "Алгоритмы и алгоритмические языки", 69], 
    ["Александр", "Фамильев", "История", 65]
]

print("Введите проходной балл: ")
score = int(input())
studentSort(stud, score)