from io import StringIO

a, b = map(int, input().strip().split(" "))

buffer = StringIO()
for i in range(b):
    buffer.write("*" * a)
    buffer.write("\n")
print(buffer.getvalue())
