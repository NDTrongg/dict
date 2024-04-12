import math
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
		dic_b[i]=math.sqrt(i)
	return dic_b
def scp(i):
	for j in range(i+1):
		if j==0:
			continue
		else:
			if j**2 ==i:
				return 1
	return 0
scp1=list(i for i in m if scp(i)==1)
if not scp1:
	print(scp1)
else:
	print(dic_a(scp1))
scp2=list(i for i in m if scp(i)==0)
if not scp2:
	print("")
else:
	print("cac so khong phai scp",(scp2))
