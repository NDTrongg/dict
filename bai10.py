import math

def solve_quadratic_equation(a, b, c):
    delta = b**2 - 4*a*c
    if delta < 0:
        return None
    elif delta == 0:
        x = -b / (2*a)
        return (x,)
    else:
        x1 = (-b + math.sqrt(delta)) / (2*a)
        x2 = (-b - math.sqrt(delta)) / (2*a)
        return (x1, x2)

def create_tuples(a, b, c, d):
    return [(a, b, c), (a, b, d), (a, c, d), (b, c, d)]

# Nhập 4 số a, b, c, d
a = float(input("Nhập số a: "))
b = float(input("Nhập số b: "))
c = float(input("Nhập số c: "))
d = float(input("Nhập số d: "))

# Tạo danh sách các tuple có độ dài 3 từ 4 số vừa nhập
tuples = create_tuples(a, b, c, d)
print("Các tuple có độ dài bằng 3 từ 4 số vừa nhập:")
for tpl in tuples:
    print(tpl)
print()

# In ra các phương trình bậc 2 có 2 nghiệm phân biệt với các hệ số trong tổ hợp a, b, c, d
print("Các phương trình bậc 2 có 2 nghiệm phân biệt:")
for tpl in tuples:
    solutions = solve_quadratic_equation(*tpl)
    if solutions is not None and len(solutions) == 2:
        print(f"Phương trình {tpl}:")
        print(f"Nghiệm x1: {solutions[0]}")
        print(f"Nghiệm x2: {solutions[1]}")
        print()