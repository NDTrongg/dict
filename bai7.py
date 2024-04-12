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
def tong_am(m):
	s=0
	s1=0
	for i in m:
		if i>0:
			s+=i
		else:
			s1+=i
	return s,s1
def tao_dic(m):
	dic_a={}
	for i in m:
		if i<0:
			dic_a['Am']=dic_a.get('Am',0)+1
		elif i>0:
			dic_a['Duong']=dic_a.get('Duong',0)+1
	dic_b={}
	for key,dem in dic_a.items():
		if key == 'Am':
			dic_b[dem]=tong_am(m)[0]
		elif key == 'Duong':
			dic_b[dem]= tong_am(m)[1]
	return dic_b
s,s1 = tong_am(m)
print(f"Tong am {s1}, tong duong {s}")
print(tao_dic(m))