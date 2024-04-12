m=[]
while 1:
    try:
        num=input("Nhap phan tu:")
        if num=='t':
            print("mang",m)
            break
        a=float(num)
        m.append(a)
    except ValueError:
        print("Nhap lai")
def tim_max_am_min_duong(m):
    max_am=None
    min_duong=None
    for i in m:
        if i<0 and (max_am  is None or i>max_am):
            max_am=i
        elif i>0 and (min_duong is None or i<min_duong):
            min_duong=i
    return {'Max am':max_am,'Min duong':min_duong}
def tinh_tbc(m):
    tong_am = 0
    tong_duong =0
    dem_am =0
    dem_duong=0
    for i in m:
        if i<0:
            tong_am+=i
            dem_am+=1
        elif i>0:
            tong_duong+=i
            dem_duong+=1
    tbc_am=tong_am/dem_am if dem_am >0 else 0
    tbc_duong= tong_duong/dem_duong if dem_duong >0 else 0
    return {'tbc am':tbc_am,'tbc duong':tbc_duong}
max_min_dict=tim_max_am_min_duong(m)
print("dic chua so am lon nhat va so duong nho nhat:",max_min_dict)
tbc=tinh_tbc(m)
print("dict chua tbc so am/so duong:",tbc)
print(tim_max_am_min_duong(m))
tup=(max_min_dict['Max am'],max_min_dict['Min duong'])
print("Tuple chua max am va min duong",tup)
