from datetime import datetime
import math, cmath

# menu
PHEP_TINH= (
    "Phép tính cơ bản",
    "Lũy thừa",
    "Căn bậc hai",
    "Hàm lượng giác",
    "Logarit",
    "Tìm số lớn nhất trong ba số",
    "Giải phương trình bậc 2",
    "Thời gian hiện tại",
    "Hiển thị lịch sử tính toán",
    "Thoát chương trình"
)

def safe_float_input(prompt: str) -> float:
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Vui lòng nhập số hợp lệ.")

def nhap_so() -> tuple[float,float]:
    return safe_float_input("Nhập số thứ nhất (x): "), safe_float_input("Nhập số thứ hai (y): ")

def get_coefficients() -> tuple[float, float, float]:
    return safe_float_input("Nhập vào hệ số a: "), safe_float_input("Nhập vào hệ số b: "), safe_float_input("Nhập vào hệ số c: ")

def solve_linear(a: float, b: float) -> str:
    """Giải phương trình ax + b = 0"""
    if a == 0:
        if b == 0:
            return "Phương trình vô số nghiệm"
        else:
            return "Phương trình vô nghiệm"
    return f"Nghiệm của phương trình là: x = {-b/a}"

def calc_discriminant(a: float, b: float, c: float) -> tuple[float, float | complex]:
    """Tính delta và căn delta phương trình bậc 2"""
    delta = b**2 - 4*a*c
    sqrt_delta = math.sqrt(delta) if delta >= 0 else cmath.sqrt(delta)
    return delta, sqrt_delta

def solve_quadratic(a: float, b: float, c: float) -> str:
    """Giải phương trình bậc 2"""
    if a == 0:
        return solve_linear(b, c)
    
    delta, sqrt_delta = calc_discriminant(a, b, c)
    if delta == 0:
        x = -b / (2*a)
        return f"Phương trình có nghiệm kép: x = {x}"
    elif delta < 0:
        x1 = (-b + sqrt_delta) / (2*a)
        x2 = (-b - sqrt_delta) / (2*a)
        return f"Phương trình có 2 nghiệm phức phân biệt:\nx1 = {x1}\nx2 = {x2}"
    else:
        x1 = (-b + sqrt_delta) / (2*a)
        x2 = (-b - sqrt_delta) / (2*a)
        return f"Phương trình có 2 nghiệm thực phân biệt:\nx1 = {x1}\nx2 = {x2}"

def input_history(history:list, cal: str, input: str, output: str) -> list:
    history.append({"calculation": cal, "input": input, "output": output})
    return history

def print_history(history: list) -> None:
    print("\n--- Calculation History ---")
    if not history:
        print("Chưa có lịch sử tính toán nào.")
    else:
        # in tiêu đề cột
        print(f"{'STT':<5} {'Phép tính':<30} {'Input':<30} {'Output':<30}")
        print("-" * 120)
        # in từng dòng lịch sử
        for i, record in enumerate(history, start=1):
            print(f"{i:<5} {record['calculation']:<30} {record['input']:<30} {record['output']:<30}")

def chon_phep_tinh() -> int:
    print("\n--- Simple calculator ---")
    for i, pt in enumerate(PHEP_TINH, start=1):
        print(f"{i}. {pt}")
    return int(input("Chọn phép tính: "))

