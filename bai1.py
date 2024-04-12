m=[]
while 1:
	try:
		num=input("Nhap so nguyen(nhap t de ket thuc):")
		if num =='t':
			print("mang",m)
			break
		a=int(num)
		m.append(a)
	except ValueError:
		print("Nhap lai")
def dic_a(m):
	dic_b={}
	for i in m:
		dic_b[i]=i*i
	return dic_b
def snt(i):
	d=0
	for j in range(i):
		if j==0:
			continue
		else:
			if i % j==0:
				d+=1
	if d==1:
		return 1
	return 0
print("dict:", dic_a(m))
sntt=list(i for i in m if snt(i)==1)
if not sntt:
	print("khong co snt")
else:
	print("so nguyen to la:",(sntt))

