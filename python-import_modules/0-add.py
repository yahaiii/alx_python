#!/usr/bin/python3
a = 1
b = 2

from add_0 import add

result = add(a, b)

print ("{} + {} = {}".format(a, b, result))

# Check if the script is being run directly
if __name__ == "__main__":
    main()