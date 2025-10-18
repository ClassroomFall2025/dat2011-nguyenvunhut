# interface

MENU_OPTIONS = {
    1: "Phép tính cơ bản",
    2: "Lũy thừa",
    3: "Căn bậc hai",
    4: "Hàm lượng giác",
    5: "Logarit",
    6: "Tìm số lớn nhất trong ba số",
    7: "Giải phương trình bậc 2",
    8: "Thời gian hiện tại",
    9: "Hiển thị lịch sử tính toán",
    10: "Thoát chương trình"
}

def display_menu() -> int:
    """Display menu and choosing function"""
    print("\n--- MÁY TÍNH ĐA NĂNG ---")
    for key, value in MENU_OPTIONS.items():
        print(f"{key}. {value}")
    
    while True:
        try:
            choice = int(input("Vui lòng chọn một chức năng: "))
            if choice in MENU_OPTIONS:
                return choice
            else:
                print("Lựa chọn không có trong menu. Vui lòng chọn lại.")
        except ValueError:
            print("Vui lòng nhập một số nguyên hợp lệ.")

def get_safe_float(prompt: str) -> float:
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Giá trị nhập không phải là số. Vui lòng nhập lại.")

def get_two_numbers() -> tuple[float, float]:
    x = get_safe_float("Nhập số thứ nhất (x): ")
    y = get_safe_float("Nhập số thứ hai (y): ")
    return x, y

def get_quadratic_coefficients() -> tuple[float, float, float]:
    print("Giải phương trình ax^2 + bx + c = 0")
    a = get_safe_float("Nhập hệ số a: ")
    b = get_safe_float("Nhập hệ số b: ")
    c = get_safe_float("Nhập hệ số c: ")
    return a, b, c