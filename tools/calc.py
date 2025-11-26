import sys

if __name__ == "__main__":
    # 参数数量检查：calc.py + 操作 + 数字1 + 数字2 = 4 个
    if len(sys.argv) != 4:
        print("用法: python3 calc.py [add|sub|mul|div] 数字1 数字2")
        sys.exit(1)

    op = sys.argv[1]      # 操作：add / sub / mul / div
    a_str = sys.argv[2]   # 第一个数字（字符串）
    b_str = sys.argv[3]   # 第二个数字（字符串）

    # 转成浮点数，支持小数
    a = float(a_str)
    b = float(b_str)

    if op == "add":
        result = a + b
    elif op == "sub":
        result = a - b
    elif op == "mul":
        result = a * b
    elif op == "div":
        result = a / b
    else:
        print("未知操作：", op)
        sys.exit(1)

    print("结果:", result)
