
m=[]
while 1:
	try:
		num=input("Nhap phan tu:")
		if num == 't':
			print("mang la:",m)
			break
		a=int(num)
		m.append(a)
	except ValueError:
		print("Nhap lai")
def dic_a(m):
	dic_b={}
	for i in m:
		if i<i+1:
			dic_b[i]=i+1
	return dic_b
def giai_thua(m):
	gt=[]
	for i in m:
		g=1
		if i>=0:
			for i in range(1,i+1):
				g*=i
		gt.append(g)
	return gt
print(dic_a(m))
print(giai_thua(m))


