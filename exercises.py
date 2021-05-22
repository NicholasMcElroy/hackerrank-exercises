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