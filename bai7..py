'''Viết một chương trình tìm tất cả các số chính phương trong đoạn 100 và 2000 (tính
cả 2 số này) và số đó phải có ít nhất 2 chữ số là số chẵn. In các số tìm được thành chuỗi
cách nhau bởi dấu phẩy, trên một dòng.'''
import math

def la_so_chinh_phuong(n):
    can_bac_hai = int(math.sqrt(n))
    return can_bac_hai * can_bac_hai == n

def dem_chu_so_chan(n):
    chu_so_chan = [int(chu_so) for chu_so in str(n) if int(chu_so) % 2 == 0]
    return len(chu_so_chan)

# Tạo danh sách các số chính phương từ 100 đến 2000
so_chinh_phuong_hop_le = []

for n in range(100, 2001):
    if la_so_chinh_phuong(n) and dem_chu_so_chan(n) >= 2:
        so_chinh_phuong_hop_le.append(str(n))

# In các số tìm được, cách nhau bởi dấu phẩy
print(','.join(so_chinh_phuong_hop_le))
