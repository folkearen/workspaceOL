a = [1,2,3,3,'a',"b"]
b = [3, 'a','b'] 
def array_diff(a,b):
    for i in b:
        while i in a:
            a.remove(i)
    return a

    #Otra forma
    def array_diff(a, b):
        return [x for x in a if x not in b]

print(array_diff(a,b))