#Chương trình quản lý học viên
#C R U D
#C: Create   (Tạo các học viên) 
#R: Read     (Hiển thị danh sách học viên)
#U: Update   (Sửa thông tin học viên)
#D: Delete   (Xóa học viên)

#Tkinter
#Bấm phím số:
#Có sự lựa chọn, chương trình chạy mãi
print("1. Thêm học viên")
print("2. Hiển thị danh sách học viên")
print("3. Sửa thông tin học viên")
print("4. Xóa học viên")
print("0. Thoát")
nhap = int(input("Nhập chức năng muốn chọn: "))
if(nhap==1):
    print("Them hoc vien")
elif(nhap==2):
    print("Hien thi danh sach")
elif(nhap==3):
    print("Sua thong tin hoc vien")
elif(nhap==4):
    print("Xóa")
elif(nhap==4):
    print("Thoát")
else:
    print("Nhap sai, yêu cầu nhập lại")