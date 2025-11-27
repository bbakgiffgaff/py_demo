import sys
from helper import welcome, add

if __name__ == "__main__":
    print("命令行参数列表:", sys.argv)

    message = welcome("Lee")
    result = add(2, 3)ooew

    print(message)
    print("2 + 3 =", result)
