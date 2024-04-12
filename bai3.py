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
def tong_chan_le(m):
	s=0
	s1=0
	for i in m:
		if i%2==0:
			s+=i
		else:
			s1+=i
	return s,s1
print(dic_a(m))
print(tuple(tong_chan_le(m)))

