"""
Escribe una función que devuelva el área de superficie total y el volumen de una caja como un arreglo:[area, volume]
"""



def get_size(w,h,d):
     return [2*(d*w + d*h + h*w),  w*h*d]

print(get_size(1, 2, 2))