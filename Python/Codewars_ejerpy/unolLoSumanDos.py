def two_sum(numbers, target):
    for index1,n1 in enumerate(numbers):
        for index2,n2 in enumerate(numbers):
            if n1 + n2 == target and index1 != index2:
                return (index1,index2)
                

print(two_sum([2,2,3], 4))