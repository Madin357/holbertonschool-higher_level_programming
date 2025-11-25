#!/usr/bin/python3
BaseGeometry = __import__('7-base_geometry').BaseGeometry

bg = BaseGeometry()

print(bg)

try:
    bg.area()
except Exception as e:
    print("[{}] {}".format(type(e).__name__, e))

# integer_validator tests
try:
    bg.integer_validator("age")
except Exception as e:
    print("[{}] {}".format(type(e).__name__, e))

try:
    bg.integer_validator("age", (4,))
except Exception as e:
    print("[{}] {}".format(type(e).__name__, e))

try:
    bg.integer_validator("age", [3])
except Exception as e:
    print("[{}] {}".format(type(e).__name__, e))

try:
    bg.integer_validator("age", True)
except Exception as e:
    print("[{}] {}".format(type(e).__name__, e))

try:
    bg.integer_validator("age", {3, 4})
except Exception as e:
    print("[{}] {}".format(type(e).__name__, e))

try:
    bg.integer_validator("age", None)
except Exception as e:
    print("[{}] {}".format(type(e).__name__, e))

try:
    bg.integer_validator("age", 0)
except Exception as e:
    print("[{}] {}".format(type(e).__name__, e))

try:
    bg.integer_validator("age", -5)
except Exception as e:
    print("[{}] {}".format(type(e).__name__, e))

# Valid case (should print nothing)
bg.integer_validator("age", 5)
