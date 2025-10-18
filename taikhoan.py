import re

def format_currency(amount):
    """Formats a number as currency with commas and two decimal places."""
    return f"{amount:,.2f} VND" #format Việt Nam đồng

class TaiKhoan:
    """
    Represents a bank account with basic attributes and methods.
    """
    def __init__(self, so_tai_khoan: str, ten: str, loai: str, so_du: float):
        """
        Initializes a new bank account.
        """
        self._so_tai_khoan = so_tai_khoan
        self._ten = ten
        self._loai = loai.upper()
        self._so_du = float(so_du)

    #getters
    @property
    def so_tai_khoan(self) -> str:
        return self._so_tai_khoan
    @property
    def ten(self) -> str:
        return self._ten
    @property
    def loai(self) -> str:
        return self._loai
    @property   
    def so_du(self) -> float:
        return self._so_du
    @property
    def to_dict(self) -> dict:
        return {
            'so_tai_khoan': self._so_tai_khoan, # Changed to match CSV header
            'ten': self._ten,
            'loai': self._loai,
            'so_du': self._so_du # Changed to match CSV header
        }
    
    #setters
    @so_tai_khoan.setter
    def so_tai_khoan(self, value: str) -> None:

        self._so_tai_khoan = value
    @ten.setter
    def ten(self, value: str) -> None:
        self._ten = value
    @loai.setter
    def loai(self, value: str) -> None:
        self._loai = value.upper()
    @so_du.setter
    def so_du(self, value: float) -> None:
        self._so_du = value
    
    def hien_thi_tai_khoan(self) -> None:
        """Prints the details of the account to the console."""
        print(f"{self._so_tai_khoan:<15} | {self._ten:<20} | {self._loai:<15} | {format_currency(self._so_du):<15}")

    def gui_tien(self, so_tien: float) -> bool:
        """
        Deposits a specified amount into the account.
        """
        if so_tien <= 0:
            print("Lỗi: Số tiền gửi phải lớn hơn 0.")
            return False
        self._so_du += so_tien
        return True

    def rut_tien(self, so_tien: float) -> bool:
        """
        Withdraws a specified amount from the account.
        """
        if so_tien <= 0:
            print("Lỗi: Số tiền rút phải lớn hơn 0.")
            return False
        if self._so_du >= so_tien:
            self._so_du -= so_tien
            return True
        print("Lỗi: Số dư không đủ để thực hiện giao dịch.")
        return False