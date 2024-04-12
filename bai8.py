import math
a = float(input("Nhập số a: "))
b = float(input("Nhập số b: "))
c = float(input("Nhập số c: "))
d = float(input("Nhập số d: "))
def kt_tg(a,b,c):
	if a <= 0 or b <= 0 or c <= 0:
		return False
	if a + b <= c or b + c <= a or c + a <= b:
		return False
	return True
def tinh_cv_dt(a,b,c):
	if not kt_tg(a,b,c):
		return None
	cv= a+b+c
	nua_cv= cv/2
	dt=math.sqrt(nua_cv*(nua_cv - a)*(nua_cv - c)*(nua_cv - b))
	return (cv,dt)
def tim_tam_giac(n):
	ds=[]
	for i in range(len(n)):
		for j in range(i+1,len(n)):
			for k in range(i+1,len(n)):
				a = n[i]
				b=n[j]
				c=n[k]
				if kt_tg(a,b,c):
					ds.append((a,b,c))
	return ds
tg = tim_tam_giac([a,b,c,d])
for i in tg:
	cv,dt = tinh_cv_dt(*i)
	print(f"Chu vi và diện tích của tam giác có cạnh {i}:")
	print(f"Chu vi: {cv}")
	print(f"Diện tích: {dt}")
	print()
not_tg= [i for i in tim_tam_giac([a,b,c,d]) if i not in tg]
print("To hop khong la tam giac:")
for i in not_tg:
	print(i)