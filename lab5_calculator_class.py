import math
import cmath
from datetime import datetime

class Calculator:
    def __init__(self):
        self._history = []

    def _add_to_history(self, calculation: str, user_input: str, output: str):
        record = {
            "calculation": calculation,
            "input": user_input,
            "output": output
        }
        self._history.append(record)

    def basic_operations(self, x: float, y: float) -> str:
        add_res = f"{x} + {y} = {x + y}"
        sub_res = f"{x} - {y} = {x - y}"
        mul_res = f"{x} * {y} = {x * y}"
        div_res = f"{x} / {y} = {x / y}" if y != 0 else "Không thể chia cho 0"
        
        output = f"{add_res}\n{sub_res}\n{mul_res}\n{div_res}"
        self._add_to_history("Phép tính cơ bản", f"x={x}, y={y}", output.replace('\n', ', '))
        return output

    def power(self, base: float, exponent: float) -> str:
        result = base ** exponent
        output = f"{base}^{exponent} = {result}"
        self._add_to_history("Lũy thừa", f"base={base}, exponent={exponent}", output)
        return output

    def square_root(self, num: float) -> str:
        result = math.sqrt(num) if num >= 0 else cmath.sqrt(num)
        output = f"√{num} = {result}"
        self._add_to_history("Căn bậc hai", f"num={num}", output)
        return output
    
    def trigonometric_funcs(self, angle_rad: float) -> str:
        sin_res = f"sin({angle_rad}) = {math.sin(angle_rad)}"
        cos_res = f"cos({angle_rad}) = {math.cos(angle_rad)}"
        tan_res = f"tan({angle_rad}) = {math.tan(angle_rad)}"
        
        output = f"{sin_res}\n{cos_res}\n{tan_res}"
        self._add_to_history("Hàm lượng giác", f"radian={angle_rad}", output.replace('\n', ', '))
        return output

    def logarithm(self, num: float, base: float = None) -> str:
        if base is None: # log10 và ln
            if num <= 0:
                output = "Đầu vào logarit phải > 0"
            else:
                log10_res = f"log10({num}) = {math.log10(num)}"
                ln_res = f"ln({num}) = {math.log(num)}"
                output = f"{log10_res}\n{ln_res}"
            self._add_to_history("Logarit (log10, ln)", f"num={num}", output.replace('\n', ', '))
        else: # log cơ số tùy chọn
            if num <= 0 or base <= 0 or base == 1:
                output = "Đầu vào hoặc cơ số không hợp lệ"
            else:
                result = math.log(num, base)
                output = f"log cơ số {base}({num}) = {result}"
            self._add_to_history("Logarit cơ số tùy chọn", f"num={num}, base={base}", output)
        return output

    def find_max_of_three(self, a: float, b: float, c: float) -> str:
        max_val = max(a, b, c)
        output = f"Số lớn nhất trong ({a}, {b}, {c}) là: {max_val}"
        self._add_to_history("Tìm số lớn nhất", f"a={a}, b={b}, c={c}", output)
        return output

    def solve_quadratic(self, a: float, b: float, c: float) -> str:
        user_input = f"a={a}, b={b}, c={c}"
        if a == 0:
            if b == 0:
                output = "Phương trình vô nghiệm" if c != 0 else "Phương trình vô số nghiệm"
            else:
                output = f"Phương trình tuyến tính có nghiệm: x = {-c/b}"
        else:
            delta = b**2 - 4*a*c
            if delta > 0:
                x1 = (-b + math.sqrt(delta)) / (2*a)
                x2 = (-b - math.sqrt(delta)) / (2*a)
                output = f"2 nghiệm thực phân biệt:\nx1 = {x1}\nx2 = {x2}"
            elif delta == 0:
                x = -b / (2*a)
                output = f"Nghiệm kép: x1 = x2 = {x}"
            else:
                sqrt_delta = cmath.sqrt(delta)
                x1 = (-b + sqrt_delta) / (2*a)
                x2 = (-b - sqrt_delta) / (2*a)
                output = f"2 nghiệm phức phân biệt:\nx1 = {x1}\nx2 = {x2}"

        self._add_to_history("Giải phương trình bậc 2", user_input, output.replace('\n', ', '))
        return output

    def get_current_time(self) -> str:
        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        output = f"Thời gian hiện tại: {now}"
        self._add_to_history("Thời gian hiện tại", "N/A", output)
        return output

    def display_history(self):
        print("\n--- LỊCH SỬ TÍNH TOÁN ---")
        if not self._history:
            print("Chưa có lịch sử nào.")
        else:
            print(f"{'STT':<5} {'Phép tính':<25} {'Đầu vào':<30} {'Kết quả':<40}")
            print("-" * 100)
            for i, record in enumerate(self._history, start=1):
                print(f"{i:<5} {record['calculation']:<25} {record['input']:<30} {record['output']:<40}")
        print("-" * 100)