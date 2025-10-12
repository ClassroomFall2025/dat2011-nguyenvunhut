from lab6_class import ChuNhat, Vuong, SinhVienIT, SinhVienBiz, SinhVienPoly

MENUSHAPES = {
    0: "Thoát ứng dụng",
    1: "Nhập Hình Chữ Nhật",
    2: "Nhập Hình Vuông",
    3: "In danh sách Hình Chữ Nhật",
    4: "In danh sách Hình Vuông",
    5: "In danh sách các hình"
} 



# MAJORS = {"lập trình máy tính",
#           "quản trị kinh doanh",
#           "công nghệ kỹ thuật điều khiển và tự động hóa",
#           "ứng dụng phần mềm",
#           "xử lý dữ liệu",
#           "thiết kế đồ họa",
#           "quản trị dịch vị du lịch và lữ hành",
#           "quản trị khách sạn",
#           "quản lý vận tải và dịch vụ logistics",
#           "công nghệ kỹ thuật cơ ký",
#           "tiếng trung quốc",
#           "tiếng hàn quốc",
#           "tiếng anh",
#           "tiếng nhật"}

# Validation input 
def safe_num_input(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Giá trị nhập vào không phải là một số! vui lòng nhập lại.")

# display menu base on input menu
def display_menu(menu):
    print("\n===============================")
    for key, value in menu.items():
        print(f"{key}. {value}")
    print("===============================")

# function for shape application
def input_rectangle(): 
    print("\n--- NHẬP HÌNH CHỮ NHẬT ---")
    rectangle = ChuNhat(safe_num_input("Nhập chiều rộng: "), safe_num_input("Nhập chiều dài: "))
    return rectangle

def input_square():
    print("\n--- NHẬP HÌNH VUÔNG ---")
    square = Vuong(safe_num_input("Nhập chiều dài cạnh: "))
    return square

def print_rectangles(rectangles: list):
    if not rectangles:
        print("Danh sách rỗng.")
        return
    
    for i, rect in enumerate(rectangles):
        print(f"--- Hình Chữ Nhật #{i+1} ---")
        rect.xuat()

def print_squares(squares:list):
    if not squares:
        print("Danh sách rỗng.")
        return
    
    for i, sq in enumerate(squares):
        print(f"--- Hình Vuông #{i+1} ---")
        sq.xuat()
        
def print_shapes(shapes):
    if not shapes:
        print("Danh sách rỗng!")
        return
    
    for i, shape in enumerate(shapes):
        print(f"--- Hình số #{i} ---")
        shape.xuat()

# Functions for students management application
# student_manager.py

class StudentManager:
    def __init__(self):
        self.__students = []
        self.MENUSTUDENT = {
            0: "Thoát ứng dụng",
            1: "Nhập danh sách sinh viên",
            2: "Xuất thông tin danh sách sinh viên",
            3: "Xuất danh sách sinh viên có học lực giỏi",
            4: "Sắp xếp danh sách sinh viên theo điểm"
        }

    def add_student(self, student):
        if student:
            self.__students.append(student)
            print(f"-> Đã thêm sinh viên '{student.get_name()}' vào danh sách.")
        else:
            print("-> Thao tác thêm sinh viên đã bị hủy.")

    def create_new_student(self):
        print("\n--- Nhập thông tin sinh viên mới ---")
        name = input("Họ và Tên: ").strip()
        major = input("Nhập ngành học: ").strip().lower()

        if major == 'it':
            try:
                java = safe_num_input("Điểm Java: ")
                html = safe_num_input("Điểm HTML: ")
                css = safe_num_input("Điểm CSS: ")
                return SinhVienIT(name, "IT", java, html, css)
            except ValueError as e:
                print(f"Lỗi: {e}")
                return None
        elif major == 'biz':
            try:
                mkt = safe_num_input("Điểm Marketing: ")
                sales = safe_num_input("Điểm Sales: ")
                return SinhVienBiz(name, "Business", mkt, sales)
            except ValueError as e:
                print(f"Lỗi: {e}")
                return None
        else:
            try:
                diem = safe_num_input("Điểm: ")
            except ValueError as e:
                print(f"Lỗi: {e}")
                return None
            new_student = SinhVienPoly(name, major)
            new_student.set_diem(diem)
            return new_student

    def display_all_students(self):
        print("\nDANH SÁCH TẤT CẢ SINH VIÊN")
        if not self.__students:
            print("Danh sách sinh viên hiện đang trống!")
            return
        
        for i, student in enumerate(self.__students, start=1):
            print(f"\n--- Sinh viên #{i} ---")
            student.xuat()

    def display_good_students(self):
        print("\nDANH SÁCH SINH VIÊN HỌC LỰC GIỎI")
        
        good_students_list = [student for student in self.__students if student.get_hoc_luc() == "Giỏi"]
        if not good_students_list:
            print("Không có sinh viên nào được xếp loại Giỏi.")
            return

        for i, student in enumerate(good_students_list, start=1):
            print(f"\n--- Sinh viên Giỏi #{i} ---")
            student.xuat()

    def sort_students_by_gpa(self):
        """Sắp xếp danh sách sinh viên theo điểm trung bình (GPA) giảm dần."""
        if not self.__students:
            print("Danh sách trống, không có gì để sắp xếp.")
            return
            
        self.__students.sort(key=lambda student: student.get_diem(), reverse=True)
        print("\n-> Đã sắp xếp thành công danh sách sinh viên theo điểm giảm dần.")
        self.display_all_students()

    def display_menu(self):
        print("\n===============================")
        print("   CHƯƠNG TRÌNH QUẢN LÝ SINH VIÊN")
        print("===============================")
        for key, value in self.MENUSTUDENT.items():
            print(f"{key}. {value}")
        print("===============================")



# In case there are major needed 
# def input_students(name:str, major:str):
#     if major.lower() in MAJORS:
#         student = SinhVienPoly(name, major)
#         return student
#     else:
#         print("Không tìm thấy ngành học, vui lòng nhập lại đúng tên ngành học!")
#         print("---Danh sách ngành học---")
#         for i, major in enumerate(MAJORS):
#             print(f"{i+1}. {major}")
#     return 
    
# def input_diem(student, diem:float):
#     return student.set_diem(diem)
    