import locale

locale.setlocale(locale.LC_ALL, 'vi_VN.UTF-8')

water_prices = (7500, 8800, 12000, 24000)

def safe_input_float(prompt: str) -> float:
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("The input is invalid!, please reinput: ")

def safe_input_int(prompt: str):
    while True:
        value = input(prompt).strip()
        if value.lower() == 's':
            return None
        try:
            return int(value)
        except ValueError:
            print("Vui lòng nhập đúng kiểu số nguyên!\nHoặc nhập 's' để dừng nhập số nguyên mới!")

def water_bill(volume:float, water_prices:tuple) -> float:

    if volume > 30:
        return 10 * water_prices[0] + 10 * water_prices[1] + 10 * water_prices[2] + (volume - 30) * water_prices[3]
    elif volume > 20:
        return 10 * water_prices[0] + 10 * water_prices[1] + (volume - 20) * water_prices[2]
    elif volume > 10:
        return 10 * water_prices[0] + (volume - 10) * water_prices[1]
    else:
        return volume * water_prices[0]
    
def ingredient_cal() -> dict:
    sugars = {"dau xanh": 0.04, "thap cam": 0.06, "deo": 0.05}
    beans = {"dau xanh": 0.07, "thap cam": 0.0, "deo": 0.02}
    cake_number = {}
    # Nhập và lưu số lượng bánh vào một dict
    for cake in sugars.keys():
        cake_number[cake] = safe_input_int(f"Nhập vào số lượng bánh {cake}: ")

    # Tính tổng đường và đậu dựa trên cake_number và sugar và beans đã cho
    total_sugars = sum(cake_number[cake] * sugars[cake] for cake in sugars)
    total_beans = sum(cake_number[cake] * beans[cake] for cake in beans)
    return {"sugars": total_sugars, "beans": total_beans}

def create_int_list() -> list:
    int_list = []
    print("Nhập 's' để dừng nhập số nguyên mới")
    while True:
        new_int = safe_input_int("Nhập vào một số nguyên mới: ")
        if new_int is None:
            return int_list
        int_list.append(new_int)