'''
Task :

Given the names and grades for each student in a class of  students, store them in a nested list and print the name(s) of any student(s) having the second lowest grade.

Note: If there are multiple students with the second lowest grade, order their names alphabetically and print each name on a new line.'''

def nested_list():
    temp = []
    students = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        temp = [name,score]
        students.append(temp)

    x = len(students)

    # Get the Students marks alone 
    marksheet = []
    for _ in range(x):
        marksheet.append(students[_][1])

    marksheet.sort()

    sec_low = marksheet[1]
    second_lowest_stud = []
    
    if sec_low < 0:
        for _ in marksheet:
            if _ > 0:
                sec_low = _
            else:
                pass
    
    if marksheet.count(sec_low) > 1:
        new_sec_low = []
        new_marksheet = set(marksheet)

        for i in new_marksheet:
            new_sec_low.append(i)

        sec_low = new_sec_low[1]
        for _ in range(x):
            if students[_][1] == sec_low :
                second_lowest_stud.append(students[_][0])
            else:
                pass

    else:
        for _ in range(x):
            if students[_][1] == sec_low :
                second_lowest_stud.append(students[_][0])
            else:
                pass

    second_lowest_stud.sort()
    for i in second_lowest_stud:
        print(i)

if __name__ == '__main__':
    nested_list()
