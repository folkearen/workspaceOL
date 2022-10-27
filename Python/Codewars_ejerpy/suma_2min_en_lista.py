def sum_two_smallest_numbers(numbers):
    min_1 = min(numbers)
    numbers.remove(min_1)
    min_2 = min(numbers)
    return min_1 + min_2

    #Otras formas
def sum_two_smallest_numbers(numbers):
    return sum(sorted(numbers)[:2])
    
def sum_two_smallest_numbers(num_list):
    num_list.sort()
    return num_list[0] + num_list[1]


print(sum_two_smallest_numbers([1,2,3,4]))