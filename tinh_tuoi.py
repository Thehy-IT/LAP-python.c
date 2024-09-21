"""Viết chương trình yêu cầu người dùng nhập vào ngày tháng năm sinh sau đó tính
tuổi của người đó."""
import datetime
def tuoi(ngay,thang,nam):
    #hiện tại
    now=datetime.date.today()
    ngaynow=now.day
    thangnow=now.month
    namnow=now.year

    if nam < namnow:
        old=namnow - nam
    elif nam == namnow and thang < thangnow or ( thang == thangnow and ngay < ngaynow):
        print("chuẩn bị được 1 tuổi !!!")
    else:
        print("chưa chào đời nhá !")

    return old
ngay=int(input("nhập ngày sinh: "))
thang=int(input("nhập tháng sinh: "))
nam=int(input("nhập năm sinh: "))
old=tuoi(ngay,thang,nam)
print("tuổi hiện tại của bạn là: ", old)