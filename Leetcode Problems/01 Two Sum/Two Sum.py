def solution(x,y,z):
    for i in range(0,z):
        for j in range(i+1, z):
            if x[i] + x[j] == y:
                print(f"[{i, j}]")

list1 = []
target = int(input("Enter the target value : "))
limit = int(input("Enter the list1 limit : "))

for i in range (0,limit):
    temp = int(input(f"Enter the value of list1[{i}] : "))
    list1.append(temp)

print(f"list1 : {list1}")
solution(list1, target, limit)
