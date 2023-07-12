import sys
from time import sleep

print("This is a test")
for x in range(10):
    sys.stdout.write(f"\rDoing thing {x}")
    sleep(0.5)
print("dd")
print("\rhhf")

sys.stdout.write("\rDoing thing")
