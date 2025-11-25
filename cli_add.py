import sys

# 检查参数数量是否正确
if len(sys.argv) < 3:
    print("用法：python3 cli_add.py 数字1 数字2")
    sys.exit(1)

a_str = sys.argv[1]  # 第一个参数
b_str = sys.argv[2]  # 第二个参数

# 命令行传进来的都是字符串，需要转成整数
a = int(a_str)
b = int(b_str)

result = a + b

print(f"你输入的是 {a} 和 {b}")
print("它们的和是：", result)
