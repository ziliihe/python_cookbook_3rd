import sys
import io

print(sys.stdout.encoding)
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding='latin-1')
print(sys.stdout.encoding)

f = open('resource/b.txt', 'w')
b = f.detach()
print(f)
print(b)

#f.write('hello')
f = io.TextIOWrapper(b, encoding='latin-1')
print(f)
f.write('hello')
