def to_celcius(x):
    return (x - 32)*5/9

for x in range (0, 101, 10):
    print("{:>3} F \ {:>6.2f} C".format(x, to_celcius(x)))