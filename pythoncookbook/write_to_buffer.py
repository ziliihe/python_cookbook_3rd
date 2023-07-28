# 将字节数据写入文本文件
import sys

print(sys.stdout.buffer.write(b'hello\n'))
