def run():
    # squares = []
    # for i in range(1, 101):
    #     squares.append(i**2)
    # print(squares)

    squaress = [ i**2  if i % 3 != 0  else "A"  for i in range(1, 101) ]
    print(squaress)

def k():
    k = [i for i in range(1,10000) if i % 36 == 0 ]
    # O if i % 4 == 0 and i % 6 == 0 and i % 9 == 0 
    print(k)


if __name__=='__main__':
    run()
    k()