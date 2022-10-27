for left in range(7):
    for right in range(left,7):#La clave esta en est left, no empieza de cero sino del valor que tiene el primer for
        print("[" + str(left) + "|" + str(right) + "]", end = " ")
    print()