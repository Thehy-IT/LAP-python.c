numbers = [1,2,3,4,5]
print(numbers)#in ra các giá trị number
print(numbers[0])#in ra số đầu tiên của mảng

numbers[1]=10#gán 10 cho mảng numbers vị trí thứ 1 thành 10
print(numbers)

print(len(numbers))# len : tính độ dài của danh sách

#vòng lặp for
for num in numbers:
    print(num)

numbers.append(6)#thêm 1 phần tử vào cuoi dan sach
print(numbers)

#xóa 1 phần tử dựa và giá trị 
numbers.remove(3)
print(numbers)

#xóa 1 phần tử dựa vào chỉ số
del numbers[1]
print(numbers)

#khởi tạo 1 set các số nguyên 
#set có thể tự loại bỏ các kí tự số chữ trùng lặp
set1 ={1,2,3,4,5}
print(set1)
set2= {1,1,2,2,2,3,4,5}
print(set2)
#kiểm tra phần tử này có trong phàn tử kia hay khong
print(3 in set1)#output true
print(10 in set2)#output false

#duyet qua tung phan tu của set
for hyhy in set1:
    print(hyhy)

#thêm phàn tư vào set
set1.add(6)
#xóa: set1.remove(6)
print(set1)

#hợp 2 set lại vs nhau
hop = set1.union(set2)
print(hop)

#điểm chung giữa 2 set
chung= set1 .intersection(set2)
print(chung)

"""tạo 1 tuple (một kiểu dữ liệu dùng để lưu trữ một tập hợp các phần tử có thứ tự.
khong the thêm xóa """
ca_nhan= ('thehy',19,'male')
print(ca_nhan)

#chỉ số dùng [] phần tử dùng{}
#truy cap các phần tử trong tuple bằng chỉ số
print(ca_nhan[0])

for item in ca_nhan:
    print(item)

#độ dài của tuple
print(len(ca_nhan))

# khai báo 1 dictionary
ca_nhan = {'name':'huynhthehy', 'age':30, 'gender':'male'}
#truy cập zá trị thông qua khóa
print(ca_nhan['name'])

#THÊM CẶP KHÓA
ca_nhan['city']='HCM'
print(ca_nhan)

#thay đổi giá trị của khóa
ca_nhan['age']=20
print(ca_nhan['age'])

#xóa 
del ca_nhan['city']
print(ca_nhan)

#kiem tra có ton tai hay hkok
print('age' in ca_nhan)

#duyetj qua tung cặp khóa
for key, value in ca_nhan.items():
    print(f'{key}:{value}')
