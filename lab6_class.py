class ChuNhat:
    def __init__(self, width, length):
        self.set_width(width)
        self.set_length(length)
    
    def get_width(self) -> float:
        return self.__width
    
    def get_length(self) -> float:
        return self.__length
    
    def width(self, _width:float):
        if _width < 0:
            raise ValueError("Width can't be less than zero!")
        self.__width = _width

    def set_length(self, _length:float):
        if _length < 0:
            raise ValueError("Length can't be less than zero!")
        self.__length = _length


    
    def perimeter(self) -> float:
        return (self.__width + self.__length) * 2
    
    def square(self) -> float:
        return (self.__width * self.__length)
    
    def xuat(self):
        print("-" * 30)
        print(f"Type: Rectangle")
        print(f"Width: {self.get_width():.2f}")
        print(f"Length: {self.get_length():.2f}")
        print(f"Perimeter: {self.perimeter():.2f}")
        print(f"Area: {self.square():.2f}")
        print("-" * 30)

class Vuong(ChuNhat):
    def __init__(self, side):
        super().__init__(side, side)

    def xuat(self):
        # The side of a square equals both the width and length of a rectangle.
        print("-" * 30)
        print(f"Type: Square")
        print(f"Side: {self.get_length():.2f}")
        print(f"Perimeter: {self.perimeter():.2f}")
        print(f"Area: {self.square():.2f}")
        print("-" * 30)


class SinhVienPoly():
    def __init__(self, name: str, major: str):
        if not name or not major:
            raise ValueError("Họ tên và ngành không được để trống!")
        self.__name = name
        self.__major = major
        self.__gpa = None

    # Getters
    def get_name(self) -> str:
        return self.__name

    def get_major(self) -> str:
        return self.__major

    def get_diem(self) -> float:
        return self.__gpa

    def get_hoc_luc(self) -> str:
        diem = self.get_diem()
        if diem < 5:
            return "Yếu"
        elif diem < 7:
            return "Trung bình"
        elif diem < 8:
            return "Khá"
        elif diem < 9:
            return "Giỏi"
        else:
            return "Xuất sắc"

    # Setters
    def set_diem(self, diem:float):
        if not 0 <= diem <= 10:
            raise ValueError("Điểm phải nằm trong khoảng 0 đến 10!")
        else: 
            self.__gpa = diem

    def xuat(self):
        print(f"{'*' * 50}")
        print(f"Họ tên     : {self.get_name()}")
        print(f"Ngành học  : {self.get_major()}")
        if not self.__gpa:
            print("Sinh viên chưa ghi nhận điểm số!")
        else:
            print(f"Điểm       : {self.get_diem():.2f}")
            print(f"Học lực    : {self.get_hoc_luc()}")
        print(f"{'*' * 50}")


class SinhVienIT(SinhVienPoly):
    def __init__(self, name:str, major:str, java:float, html:float, css:float):
        super().__init__(name, major)
        for score in (java, html, css):
            if not (0 <= score <= 10):
                raise ValueError("Điểm phải từ 0 đến 10!")
        self.__java = java
        self.__html = html
        self.__css = css
        self.set_diem()

    def get_diem(self) -> float:
        return (2 * self.__java + self.__html + self.__css) / 4
    
    def set_diem(self) -> float:
        return super().set_diem(self.get_diem())
    
class SinhVienBiz(SinhVienPoly):
    def __init__(self, name:str, major:str, marketing:float, sales:float):
        super().__init__(name, major)
        for score in (marketing, sales):
            if not (0 <= score <= 10):
                raise ValueError("Điểm phải từ 0 đến 10!")
        self.__marketing = marketing
        self.__sales = sales
        self.set_diem()

    def get_diem(self) -> float:
        return (2 * self.__marketing + self.__sales) / 3
    
    def set_diem(self) -> float:
        return super().set_diem(self.get_diem())
      
# class SinhVienPoly:
#     __slots__ = ("_name", "_major", "_gpa", "_performance")

#     def __init__(self, name: str, major: str, gpa: float = 0.0):
#         if not name or not major:
#             raise ValueError("Name and major cannot be empty.")
#         if not (0 <= gpa <= 10):
#             raise ValueError("GPA must be between 0 and 10.")
#         self._name = name
#         self._major = major
#         self._gpa = gpa
#         self._performance = self._evaluate_performance(gpa)

#     @staticmethod
#     def _evaluate_performance(gpa: float) -> str:
#         if gpa < 5:
#             return "Weak"
#         elif gpa < 7:
#             return "Average"
#         elif gpa < 8:
#             return "Good"
#         elif gpa < 9:
#             return "Very Good"
#         return "Excellent"

#     # properties (fast, clean, Pythonic)
#     @property
#     def name(self): return self._name

#     @property
#     def major(self): return self._major

#     @property
#     def gpa(self): return self._gpa

#     @property
#     def performance(self): return self._performance

#     def __str__(self):
#         return (f"{self._name:20} | {self._major:15} | "
#                 f"GPA: {self._gpa:4.2f} | {self._performance}")


# class SinhVienIt(SinhVienPoly):
#     __slots__ = ("_java", "_html", "_css")

#     def __init__(self, name: str, java: float, html: float, css: float):
#         self._validate_scores(java, html, css)
#         gpa = (2 * java + html + css) / 4
#         super().__init__(name, "IT", gpa)
#         self._java, self._html, self._css = java, html, css

#     @staticmethod
#     def _validate_scores(*scores):
#         if not all(0 <= s <= 10 for s in scores):
#             raise ValueError("Scores must be between 0 and 10.")


# class SinhVienBiz(SinhVienPoly):
#     __slots__ = ("_marketing", "_sales")

#     def __init__(self, name: str, marketing: float, sales: float):
#         self._validate_scores(marketing, sales)
#         gpa = (2 * marketing + sales) / 3
#         super().__init__(name, "Business", gpa)
#         self._marketing, self._sales = marketing, sales

#     @staticmethod
#     def _validate_scores(*scores):
#         if not all(0 <= s <= 10 for s in scores):
#             raise ValueError("Scores must be between 0 and 10.")
