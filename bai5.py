def xuli_chuoi(chuoi):
    cac_tu= chuoi.split()
    
    cac_tu= list(set(cac_tu))
    
    cac_tu.sort(key=str.lower)#sap xep chu cai 
    
    for i in range(len(cac_tu)):
        if cac_tu[i][0].lower()=='a':
            cac_tu[i]= cac_tu[i].capitalize()
    return ' '.join(cac_tu)

#nhap chuoi tu ban phim
chuoi=input("nhap chuoi cach nhau boi khoang trang: ")
ket_qua=xuli_chuoi(chuoi)
print("ket qua sau khi xu li la: ", ket_qua)