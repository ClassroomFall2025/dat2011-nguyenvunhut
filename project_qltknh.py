from quanlynganhang import QuanLyTaiKhoan

qltk = QuanLyTaiKhoan()

while True:
    qltk.hien_thi_menu()
    choice = int(input("Nhập lựa chọn của bạn: "))

    match choice:
        case 0: 
            print("Tạm biệt!")
            break
        case 1:
            qltk.them_tk()
        case 2:
            qltk.gui_tien_vao_tk()
        case 3:
            qltk.rut_tien_tu_tk()
        case 4:
            qltk.kiem_tra_so_du()
        case 5:
            qltk.danh_sach_all_tk()
        case 6:
            qltk.dong_tk()
        case 7:
            qltk.chinh_sua_tk()
        case 8:
            qltk.tim_kiem_theo_ten()
        case 9:
            qltk.xuat_bao_cao()
        case 10:
            qltk.sao_luu()
        case 11:
            qltk.khoi_phuc()
        case _:
            print("Chức năng không tồn tại, vui lòng nhập lại!")