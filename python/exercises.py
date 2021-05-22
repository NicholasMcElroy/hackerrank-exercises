'''
Given the participants' score sheet for your University Sports Day, you are required to find the runner-up score.
You are given scores. Store them in a list and find the score of the runner-up.
'''

if __name__ == '__main__':
    n = int(input())
    arr = input().split()
    length = len(arr)
    i = 0
    for i in range(0, length):
        arr[i] = int(arr[i])
    no1 = max(arr)
    no2 = min(arr)
    for i in range(0, length):
        if arr[i] < no1:
            if arr[i] >= no2:
                no2 = arr[i]
    print(no2)

'''Given an integer, n, perform the following conditional actions:

    If n is odd, print Weird
    If n is even and in the inclusive range of 2 to 5, print Not Weird
    If n is even and in the inclusive range of 6 to 20, print Weird
    If n is even and greater than 20, print Not Weird
'''
if __name__ == '__main__':
    n = int(input().strip())
    if (n % 2 != 0):
        print("Weird")
    elif (n >= 2) and (n <= 5) and (n % 2 == 0):
        print("Not Weird")
    elif (n >= 6) and (n <= 20) and (n % 2 == 0):
        print("Weird")
    elif (n > 20) and (n % 2 == 0):
        print("Not Weird")

'''Given a year, determine whether it is a leap year. If it is a leap year, 
return the Boolean True, otherwise return False.

Note that the code stub provided reads from STDIN and passes arguments to the is_leap function. 
It is only necessary to complete the is_leap function. '''


def is_leap(year):
    leap = False
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                leap = True
            else:
                leap = False
        else:
            leap = True
    else:
        leap: False
    return leap

'''Given the names and grades for each student in a class of students, 
store them in a nested list and print the name(s) of any student(s) having the second lowest grade.'''

if __name__ == '__main__':
    students = []
    scores = set()

    for _ in range(int(input())):
        name = input()
        score = float(input())
        students.append([name, score])
        scores.add(score)

    second_low = sorted(scores)[1]
    second_low_students = []

    for name, score in students:
        if score == second_low:
            second_low_students.append(name)

    for name in sorted(second_low_students):
        print(name)

''' You are given three integers x, y, and z representing the dimensions of a cuboid along with an integer n. 
Print a list of all possible coordinates given by (i, j, k) on a 3D grid where the sum of i + j + kis not equal to n. 
Here, 0 <= i <= x, 0 <= j <= y. 0 <= k <= z.
'''
X = int(input())
Y = int(input())
Z = int(input())
N = int(input())

X += 1
Y += 1
Z += 1

ijk = [[x, y, z] for x in range(X) for y in range(Y) for z in range(Z) if x + y + z != N]
print(ijk)

'''The provided code stub will read in a dictionary containing key/value pairs of name:[marks] for a list of students. 
Print the average of the marks array for the student name provided, showing 2 places after the decimal. '''
if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    query_avg = sum(student_marks[query_name])
    query_avg = query_avg / len(student_marks[query_name])
    print("{:0.2f}".format(query_avg))

'''You are given a positive integer N. Print a numerical triangle of height N - 1 like the one below:

1
22
333
4444
55555
......

Can you do it using only arithmetic operations, a single for loop and print statement?

Use no more than two lines.'''

for i in range(1,int(input())): #More than 2 lines will result in 0 score. Do not leave a blank line also
    print(int(i * (10 ** i)/9))
