b = 'b\udece4d.txt'

try:
    print(b)
except UnicodeEncodeError:
    print(1)