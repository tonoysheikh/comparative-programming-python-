import math

a, b = map(float, input().split())

print("floor", int(a), "/", b, "=", math.floor(a / b))
print("ceil", a, "/", b, "=", math.ceil(a / b))
print("round", a, "/", b, "=", round(a / b))