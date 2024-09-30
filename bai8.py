'''Viết một chương trình nhập vào một câu sau đó đếm xem có bao nhiêu chữ hoa, bao
nhiêu chữ thường.'''
cau=input("nhap vao 1 cau : ")

chu_hoa= 0
chu_thuong=0

for ki_tu in cau:
    if ki_tu.isupper():
        chu_hoa += 1
    elif ki_tu.islower():
        chu_thuong +=1
        
print("so chux thuong la: ",chu_thuong)
print("so chu hoa la: ",chu_hoa)