a=[0,0,0,0,0,0,0]
#sisi pengirim
a[2]=1
a[4]=1
a[5]=0
a[6]=1

a[0]=a[2]^a[4]^a[6]
a[1]=a[2]^a[5]^a[6]
a[3]=a[4]^a[5]^a[6]
print ("codeword yang dikirim",a)

#sisi penerima
b=[1, 1, 0, 0, 1, 0, 1]
print ("codeword yang di terima",b)
c1=b[0]^b[2]^b[4]^b[6]
c2=b[1]^b[2]^b[5]^b[6]
c3=b[3]^b[4]^b[5]^b[6]

p=c1*1+c2*2+c3*4
if p==0:
    print("tidak ada error yang terjadi")
else:
    print("terdapat error di posisi",p)
    if b[p-1]==1:
        b[p-1]=0
    else:
        b[p-1]=1
    print ("jadi codeword yang benar",b)