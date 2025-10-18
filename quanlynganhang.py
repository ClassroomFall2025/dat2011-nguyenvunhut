import csv
import os
import shutil
from datetime import datetime
import re
from string import digits
from taikhoan import TaiKhoan 

class QuanLyTaiKhoan:
    """
    Manages all account operations, including data persistence with CSV files.
    """
    DATA_FILE = 'taikhoan.csv'
    BACKUP_DIR = 'backup/'
    REPORT_DIR = 'reports/'
    FIELDNAMES = ['so_tai_khoan', 'ten', 'loai', 'so_du']

    def __init__(self):
        self._danh_sach_tai_khoan = []
        self._tao_thu_muc_neu_can(self.BACKUP_DIR) # Ensure backup directory exists
        self._tao_thu_muc_neu_can(self.REPORT_DIR) # Ensure report directory exists
        self._docTaiKhoanTuCSV()
        self._menu_options = {
        0: "Thoát chương trình",
        1: "Tạo tài khoản mới",
        2: "Gửi tiền",
        3: "Rút tiền",
        4: "Kiểm tra số dư",
        5: "Hiển thị danh sách tất cả tài khoản",
        6: "Đóng (Xóa) tài khoản",
        7: "Chỉnh sửa tài khoản",
        8: "Tìm kiếm tài khoản theo tên",
        9: "Xuất báo cáo thống kê",
        10: "Sao lưu dữ liệu",
        11: "Khôi phục dữ liệu"
    }

    # --- Private Helper Methods ---
    def _tao_thu_muc_neu_can(self, dir_path):
        if not os.path.exists(dir_path):
            os.makedirs(dir_path)

    def _docTaiKhoanTuCSV(self):
        try:
            with open(self.DATA_FILE, mode='r', newline='', encoding='utf-8') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    tk = TaiKhoan(row['so_tai_khoan'], row['ten'], row['loai'], float(row['so_du']))
                    self._danh_sach_tai_khoan.append(tk)
                print(f"Đang có {len(self._danh_sach_tai_khoan)} tài khoản!")
        except FileNotFoundError:
            pass # File doesn't exist yet, will be created on save
        except Exception as e:
            print(f"Lỗi không xác định khi đọc file: {e}")

    def _ghiTaiKhoanVaoCSV(self, new_tai_khoan: list[TaiKhoan | list]) -> bool:
        """
        Ghi danh sách tài khoản hoặc tài khoản mới vào file CSV
        """
        # if new_tai_khoan is a list then open as w
        if isinstance(new_tai_khoan, list): 
            file_exists = os.path.exists(self.DATA_FILE)
            with open(self.DATA_FILE, mode='w', newline='', encoding='utf-8') as file:
                writer = csv.DictWriter(file, fieldnames=self.FIELDNAMES)
                if not file_exists or os.stat(self.DATA_FILE).st_size == 0:
                    writer.writeheader()
                for tk in new_tai_khoan:
                    writer.writerow(tk.to_dict)
                print(f"Đã ghi {len(new_tai_khoan)} tài khoản vào file CSV")
                self._docTaiKhoanTuCSV() # Update current list 
                return True
        #if new_tai_khoan is a TaiKhoan then open as a
        elif isinstance(new_tai_khoan, TaiKhoan):
            file_exists = os.path.exists(self.DATA_FILE)
            with open(self.DATA_FILE, mode='a', newline='', encoding='utf-8') as file:
                writer = csv.DictWriter(file, fieldnames=self.FIELDNAMES)
                if not file_exists or os.stat(self.DATA_FILE).st_size == 0:
                    writer.writeheader()
                writer.writerow(new_tai_khoan.to_dict)
                print("Đã ghi tài khoản vào file CSV")
                self._docTaiKhoanTuCSV() # Update current list 
                True
        else:
            print("new_tai_khoan phải là danh sách hoặc tài khoản")
            return False 

    def _tim_tai_khoan(self, so_tk_can_tim):
        if not so_tk_can_tim.isdigit():
            print("Số tài khoản phải là dãy số!")
            return None
        for tk in self._danh_sach_tai_khoan:
            if tk.so_tai_khoan == so_tk_can_tim:
                return tk
        return None
    
    def _tao_tk(self):
        so_tk = input("Nhập số tài khoản mới: ").strip()
        if self._tim_tai_khoan(so_tk):
            print("Số tài khoản đã tồn tại, vui lòng nhập lại!")
            return None

        ten = input("Nhập tên chủ tài khoản: ").strip().title()
        
        loai_tk = input("Nhập loại tài khoản (T: Tiết kiệm, C: Thanh toán): ").strip().upper()
        if not loai_tk in ['T', 'C']:
            print("Loại tài khoản không hợp lệ, vui lòng nhập lại!")
            return None

        so_du_ban_dau = float(input("Nhập số dư ban đầu: ").strip())
        if so_du_ban_dau < 0:
            print("Số dư ban đầu phải lớn hơn hoặc bằng 0!")
            return None
        tk_moi = TaiKhoan(so_tk, ten, loai_tk, so_du_ban_dau)
        return tk_moi

    # --- Public Methods for Menu Functions ---
    def hien_thi_menu(self):
        print("--- QUẢN LÝ TÀI KHOẢN NGÂN HÀNG ---")
        for key, value in self._menu_options.items():
            print(f" {key}. {value}")

    def them_tk(self):
        print("\n--- TẠO TÀI KHOẢN MỚI ---")
        tk_moi = self._tao_tk()
        if tk_moi:
            self._danh_sach_tai_khoan.append(tk_moi)
            print(f"Đã tạo và thêm tài khoản mới '{tk_moi.ten}' thành công!")
            self._ghiTaiKhoanVaoCSV(tk_moi)
        else:
            print("Không thể tạo tài khoản mới, vui lòng nhập lại!")

    def gui_tien_vao_tk(self):
        """
        Gửi tiền vào một tài khoản cụ thể
        """
        print("\n--- GỬI TIỀN ---")
        so_tk = input("Nhập số tài khoản: ").strip()
            
        tk = self._tim_tai_khoan(so_tk)
        if not tk:
            print(f"Tài khoản {so_tk} không tồn tại!")
            return None
        so_tien = float(input("Nhập số tiền muốn gửi: "))

        if tk.gui_tien(so_tien):
            print(f"Đã gửi {so_tien} vào tài khoản {so_tk} thành công!")
            self._ghiTaiKhoanVaoCSV(self._danh_sach_tai_khoan)
        else:
            print("Gửi tiền không thành công!")
            
    def rut_tien_tu_tk(self):
        """
        Rút tiền từ một tài khoản cụ thể
        """
        print("\n--- RÚT TIỀN ---")
        so_tk = input("Nhập số tài khoản: ").strip()
            
        tk = self._tim_tai_khoan(so_tk)
        if not tk:
            print(f"Tài khoản {so_tk} không tồn tại!")
            return None
        so_tien = float(input("Nhập số tiền muốn rút:"))

        if tk.rut_tien(so_tien):
            print(f"Đã rút {so_tien} từ tài khoản {so_tk} thành công!")
            self._ghiTaiKhoanVaoCSV(self._danh_sach_tai_khoan)
        else:
            print("Rút tiền không thành công!")


    def kiem_tra_so_du(self):
        """
        Kiểm tra số dư của một tài khoản cụ thể
        """
        print("\n--- KIỂM TRA SỐ DƯ ---")
        so_tk = input("Nhập số tài khoản: ").strip()
            
        tk = self._tim_tai_khoan(so_tk)
        if not tk:
            print(f"Tài khoản {so_tk} không tồn tại!")
            return None

        print(f"Số dư của tài khoản {so_tk} là: {tk.so_du}")


    def xuat_danh_sach(self, danh_sach):
        """
        Hiển thị danh sách tài khoản được cho
        """
        print("\n--- DANH SÁCH TÀI KHOẢN ---")
        print("-"*90)
        print(f"{'Số tài khoản':<15} | {'Tên chủ tài khoản':<20} | {'Loại tài khoản':<15} | {'Số dư':<15}") 
        for tk in danh_sach:
            tk.hien_thi_tai_khoan()
    
    def danh_sach_all_tk(self):
        """
        Xuất danh sách của tất cả tài khoản
        """
        self.xuat_danh_sach(self._danh_sach_tai_khoan)



    def dong_tk(self):
        print("\n--- ĐÓNG (XÓA) TÀI KHOẢN ---")
        so_tk = input("Nhập số tài khoản: ").strip()            
        tk = self._tim_tai_khoan(so_tk)
        if not tk:
            print(f"Tài khoản {so_tk} không tồn tại!")
            return None
        else:
            print(f"Tài khoản bạn muốn xóa là: {tk.hien_thi_tai_khoan()}")
            if (comfirm := input("Xác nhận xóa tài khoản (y/n): ").strip().lower()) == 'y':
                self._danh_sach_tai_khoan.remove(tk)
                print(f"Đã xóa nhân viên {tk.ten}")
                self._ghiTaiKhoanVaoCSV(self._danh_sach_tai_khoan)
                print("Đã cập nhật lại danh sách tài khoản!")
            else:
                return None

    def chinh_sua_tk(self):
        print("\n--- CHỈNH SỬA TÀI KHOẢN ---")
        so_tk = input("Nhập số tài khoản: ").strip()
        tk = self._tim_tai_khoan(so_tk)
        if not tk:
            print(f"Tài khoản {so_tk} không tồn tại!")
            return None
        print("Thay đổi thôn tin tài khoản, để trống (enter) nếu muốn giữa nguyên:")
        if (new_stk := input(f"{tk.so_tai_khoan} số tài khoản mới: ")):
            tk.so_tai_khoan = new_stk
        if (new_ten := input(f"{tk.ten} tên mới: ")):
            tk.ten = new_ten
        if (new_loai := input(f"{tk.loai} loại mới (T/C): ")):
            tk.loai = new_loai
        if (new_so_du := input(f"{tk.so_du} số dư mới: ")):
            tk.so_du = new_so_du
        
        if self._ghiTaiKhoanVaoCSV(self._danh_sach_tai_khoan): print("Thay đổi thông tin thành công!")
        

    def tim_kiem_theo_ten(self):
        print("\n--- TÌM KIẾM THEO TÊN ---")
        search_ten = input("Nhập tên bạn cần tìm: ").strip().title()
        danh_sach = []
        for tk in self._danh_sach_tai_khoan:
            if tk.ten == search_ten:
                danh_sach.append(tk)
        if not danh_sach:
            print(f"Không có tài khoản nào có tên {search_ten}")
            return None
        else:
            self.xuat_danh_sach(danh_sach)

        
    def xuat_bao_cao(self):
        print("\n--- XUẤT BÁO CÁO ---")
        if not self._danh_sach_tai_khoan:
            print("Không có tài khoản nào để xuất báo cáo!")
        
        tong_tk = len(self._danh_sach_tai_khoan)
        tong_so_du = sum(tk.so_du for tk in self._danh_sach_tai_khoan)
        tong_tk_t = sum(1 for tk in self._danh_sach_tai_khoan if tk.loai == 'T')
        tong_so_du_t = sum(tk.so_du for tk in self._danh_sach_tai_khoan if tk.loai == 'T')
        tong_tk_c = sum(1 for tk in self._danh_sach_tai_khoan if tk.loai == 'C')
        tong_so_du_c = sum(tk.so_du for tk in self._danh_sach_tai_khoan if tk.loai == 'C')

        timestamp = datetime.now().strftime("%Y%m%d")
        file_path = os.path.join(self.REPORT_DIR, f"report_{timestamp}.txt")

        try:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write("BÁO CÁO THÔNG KÊ TÀI KHOẢN NGÂN HÀNG\n")
                f.write(f"Ngày xuất: {datetime.now().strftime('%d-%m-%Y %H:%M:%S')}\n")
                f.write("=" * 60 +"\n")
                f.write(f"Tổng số tài khoản: {tong_tk}\n")
                f.write(f"\t- Tiết kiệm: {tong_tk_t}\n")
                f.write(f"\t- Thanh toán: {tong_tk_c}\n")
                f.write("\n")
                f.write(f"Tổng số dư: {tong_so_du}\n")
                f.write(f"\t- Tiết kiệm: {tong_so_du_t}\n")
                f.write(f"\t- Thanh toán: {tong_so_du_c}\n")
                f.write("=" * 60 + "\n")
                print(f"Xuất báo cáo thành công vào file: {file_path}")
        except Exception as e:
            print(f"Lỗi xuất báo cáo {e}")

    def sao_luu(self):
        print("\n--- SAO LƯU DỮ LIỆU ---")
        if not os.path.exists(self.DATA_FILE):
            print(f"Lỗi: Không tìm thấy file dữ liệu '{self.DATA_FILE}'.")
            return
            
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        backup_file_name = f"taikhoan_{timestamp}.bak"
        backup_path = os.path.join(self.BACKUP_DIR, backup_file_name)
        
        try:
            shutil.copy(self.DATA_FILE, backup_path)
            print(f"Sao lưu dữ liệu thành công vào: {backup_path}")
        except Exception as e:
            print(f"Lỗi trong quá trình sao lưu: {e}")
    
    def khoi_phuc(self):
        print("\n--- KHÔI PHỤC DỮ LIỆU ---")
        try:
            backup_files = sorted([f for f in os.listdir(self.BACKUP_DIR) if f.endswith('.bak')])
            if not backup_files:
                print("Không tìm thấy file sao lưu nào trong thư mục 'backup/'.")
                return
            
            print("Chọn file sao lưu để khôi phục:")
            for i, filename in enumerate(backup_files):
                print(f" {i+1}. {filename}")
            
            try:
                choice = int(input("Nhập lựa chọn của bạn (0 để hủy): ").strip())
                if choice == 0:
                    print("Hủy thao tác.")
                    return
                if not 1 <= choice <= len(backup_files):
                    print("Lựa chọn không hợp lệ.")
                    return
                
                chosen_file = backup_files[choice - 1]
                xac_nhan = input(f"Cảnh báo: Sẽ ghi đè dữ liệu hiện tại. "
                                    f"Khôi phục từ '{chosen_file}'? (Nhập 'C' để xác nhận): ").strip().upper()

                if xac_nhan == 'C':
                    shutil.copy(os.path.join(self.BACKUP_DIR, chosen_file), self.DATA_FILE)
                    self._danh_sach_tai_khoan.clear()
                    self._docTaiKhoanTuCSV()
                    print("Đã khôi phục dữ liệu thành công.")
                else:
                    print("Hủy thao tác khôi phục.")
            except ValueError:
                print("Lỗi: Vui lòng nhập một số.")
                
        except Exception as e:
            print(f"Lỗi trong quá trình khôi phục: {e}")