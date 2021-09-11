import math as m

def hesapla(a,b):
    h=(a-b)/3
    ort1=a+h
    ort2=a+(2*h)

    f1=m.exp(a)
    f2=m.exp(ort1)
    f3=m.exp(ort2)
    f4=m.exp(b)

    r=((3*h)/8)*((f1+(3*f2)+(3*f3)+f4))
    return r

a=input("Üst Sınır : ")
b=input("Alt Sınır : ")

print(hesapla(float(a),float(b)))
