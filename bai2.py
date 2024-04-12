m=[]
while 1:
	try:
		num=input("Nhap phan tu:")
		if num =='t':
			print("mang la:",m)
			break
		a=int(num)
		m.append(a)
	except ValueError:
		print("Nhap lai")
def tup(m):
	return tuple(m)
def snt(i):
	d=0
	for j in range(i):
		if j==0:
			continue
		else:
			if i%j==0:
				d+=1
	if d==1:
		return 1
	return 0
print("tupple la:",tup(m))
s=list(i for i in m if snt(i)==1)
if not s:
	print("khong co snt")
else:
	print("tuple snt la:",(s))
