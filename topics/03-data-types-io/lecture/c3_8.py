import math as math
import sys as sys

x = 0.0
for i in range(0, 10, 1):
    x += 0.1
    print(x)

print(f"Same {x == 1.0}")
print(f"Cca {math.isclose(x, 1.0)}")
print(f"Roziel {1.0 - x}")

eps = 1.0

while(1.0 + eps != 1.0):
    eps /= 2

print(f"{eps} a {sys.float_info.epsilon}")
