"""Nhập 1 danh sách gồm n số nguyên (n là tùy ý, kết thúc nhập khi bấm phím ‘t’)
Viết hàm tính tổng các số từ 1 ->n
Viết hàm tạo 1 dictionary gồm key là các số nguyên và value là tổng các số từ 1 đến chính nó
Sử dụng 2 hàm đã viết:
- In ra màn hình dictionary có key là các số trong danh sách vừa nhập.
- In ra các tuple chứa tổng các số từ 1 đến từng số có trong danh sách đã nhập"""
m=[]
while 1:
	try:
		num=input("Nhap phan tu:")
		if num == 't':
			print("mang la: ",m)
			break
		a=int(num)
		m.append(a)
	except ValueError:
		print("Nhap lai")
def tinh_tong(m):
	s=0
	for i in range(len(m)):
		s+=i
	return s
def tong(n):
	return sum(range(1,n+1))
def dic(m):
	dic_a={}
	for i in m:
		dic_a[i]=tong(i)
	return dic_a
def tong_tung_so(m):
	b=[]
	for i in m:
		c=tong(i)
		b.append(c)
	return tuple(b)
print("Tong cac so trong list: ",tong_tung_so(m))
print("Dict:")
