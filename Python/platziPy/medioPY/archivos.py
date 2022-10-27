from encodings import utf_8


def read():
    numbers = []
    with open("/home/folkearen/workspace/python/platziPy/medioPY/number.txt", "r", encoding="utf8") as f:
         for line in f:
             numbers.append(int(line))
    print(numbers)

def write():
    names = ['Facundo', 'Cristian', 'Miguel', 'pepe', 'Rocío', 'Maria', 'Fenanda']
    with open("medioPY/names.txt", 'a', encoding='utf8') as f:
        for name in names:
            f.write(name)
            f.write("\n")


def run():
    read()
    write()


if __name__ == '__main__':
    run()
