from functools import reduce

print(reduce(lambda x,y:x + y,filter(lambda x: x % 2 != 0, [1,2,3,4,5,6,7,8,9])))
