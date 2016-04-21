a = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15] # <<<<-------------- INPUT
#o = [11,4,5,8,3,10,0,12,15,14,13,6,9,1,2,7] # <<<<-------------- OUTPUT
#o = [9,5,3,8,6,2,4,11,15,1,7,14,7,10,0,10] vitalik
#o = [15,3,7,13,12,9,1,11,10,0,14,2,4,5,8,6] #glushchenko
o = [7,5,9,2,6,8,15,4,1,12,13,3,10,14,0,11]
def Binary_matrix(a):
    #a -- list of base10 numbers
    b = []
    for i,index in enumerate(a):
        j = bin(int(a[i]))
        if (int(a[i]) <= 1):
            buff2 = "0" + "0" + "0" + j[2:]
            b.append(list(buff2))
        elif (int(a[i]) <= 3):
            buff1 = "0" + "0" + j[2:]
            b.append(list(buff1))
        elif (int(a[i]) <= 7):
            buff = "0" + j[2:]
            b.append(list(buff))
        else:
            buf = j[2:]
            b.append(list(buf))
    return b
h = Binary_matrix(a)
y = Binary_matrix(o)
def cut_projection(h,r):        
    #Function making cut of column(x1/x2/x3/x4 || y1/y2/y/3/y4)
    #h -- matrix where we taking cut, in our case its a function that makes matrix
    #r -- position of column that we are cutting
    b = []
    for i,index in enumerate(h):
        b.append(int(h[i][r]))
    #for i in l:
    #    print("(["+i+"])")
    return b
def zero_table(h,r):
    b = []
    for i,index in enumerate(h):
        b.append(int(h[i][r])*0)
    #for i in l:
    #    print("(["+i+"])")
    return b
def XOR2(v1,v2):
    b = []
    b1 = [] # X1 + X2 || Y1 + Y2
    for i in zip(v1,v2):
        b.append(i)
    for i,index in enumerate(b):
        b1.append((int(index[0])^int(index[1])))
    return b1
def XOR3(v1,v2,v3):
    b= []
    b1= [] # X1 + X2 + X3 || Y1 + Y2 + Y3
    for i in zip(v1, v2, v3):
            b.append(i)
    for i, index in enumerate(b):
            b1.append((int(index[0]) ^ int(index[1])) ^ int(index[2]))
    return b1
def XOR4(v1,v2,v3,v4):
    b = []
    b1 = []  # X1 + X2 + X3 || Y1 + Y2 + Y3
    for i in zip(v1, v2, v3, v4):
        b.append(i)
    for i, index in enumerate(b):
        b1.append((int(index[0]) ^ int(index[1])) ^ int(index[2]) ^ int(index[3]))
    return b1

# OUTPUT
Xor = zip(Binary_matrix(a),
          Binary_matrix(o),
          cut_projection(h, 3),
          cut_projection(h, 2),
          XOR2(cut_projection(h, 3), cut_projection(h, 2)),
          cut_projection(h, 1),
          XOR2(cut_projection(h, 1), cut_projection(h, 3)),
          XOR2(cut_projection(h, 1), cut_projection(h, 2)),
          XOR3(cut_projection(h, 1), cut_projection(h, 2), cut_projection(h, 3)),
          cut_projection(h, 0),
          XOR2(cut_projection(h, 0), cut_projection(h, 3)),
          XOR2(cut_projection(h, 0), cut_projection(h, 2)),
          XOR3(cut_projection(h, 0), cut_projection(h, 2), cut_projection(h, 3)),
          XOR2(cut_projection(h, 0), cut_projection(h, 1)),
          XOR3(cut_projection(h, 0), cut_projection(h, 2), cut_projection(h, 3)),
          XOR3(cut_projection(h, 0), cut_projection(h, 1), cut_projection(h, 2)),
          XOR4(cut_projection(h, 0), cut_projection(h, 1), cut_projection(h, 2), cut_projection(h, 3)),
          cut_projection(y, 3),
          cut_projection(y, 2),
          XOR2(cut_projection(y, 3), cut_projection(y, 2)),
          cut_projection(y, 1),
          XOR2(cut_projection(y, 1), cut_projection(y, 3)),
          XOR2(cut_projection(y, 1), cut_projection(y, 2)),
          XOR3(cut_projection(y, 1), cut_projection(y, 2), cut_projection(y, 3)),
          cut_projection(y, 0),
          XOR2(cut_projection(y, 0), cut_projection(y, 3)),
          XOR2(cut_projection(y, 0), cut_projection(y, 2)),
          XOR3(cut_projection(y, 0), cut_projection(y, 2), cut_projection(y, 3)),
          XOR2(cut_projection(y, 0), cut_projection(y, 1)),
          XOR3(cut_projection(y, 0), cut_projection(y, 2), cut_projection(y, 3)),
          XOR3(cut_projection(y, 0), cut_projection(y, 1), cut_projection(y, 2)),
          XOR4(cut_projection(y, 0), cut_projection(y, 1), cut_projection(y, 2), cut_projection(y, 3)))


for j,index in enumerate(Xor):
    print(index)

Possibility = [[0 for i in range(15)] for x in range(15)]
def test(a= None,b= None) -> object:
    Rox = zip(
    	     cut_projection(h, 3),
          cut_projection(h, 2),
          XOR2(cut_projection(h, 3), cut_projection(h, 2)),
          cut_projection(h, 1),
          XOR2(cut_projection(h, 1), cut_projection(h, 3)),
          XOR2(cut_projection(h, 1), cut_projection(h, 2)),
          XOR3(cut_projection(h, 1), cut_projection(h, 2), cut_projection(h, 3)),
          cut_projection(h, 0),
          XOR2(cut_projection(h, 0), cut_projection(h, 3)),
          XOR2(cut_projection(h, 0), cut_projection(h, 2)),
          XOR3(cut_projection(h, 0), cut_projection(h, 2), cut_projection(h, 3)),
          XOR2(cut_projection(h, 0), cut_projection(h, 1)),
          XOR3(cut_projection(h, 0), cut_projection(h, 2), cut_projection(h, 3)),
          XOR3(cut_projection(h, 0), cut_projection(h, 1), cut_projection(h, 2)),
          XOR4(cut_projection(h, 0), cut_projection(h, 1), cut_projection(h, 2), cut_projection(h, 3)),
          cut_projection(y, 3),
          cut_projection(y, 2),
          XOR2(cut_projection(y, 3), cut_projection(y, 2)),
          cut_projection(y, 1),
          XOR2(cut_projection(y, 1), cut_projection(y, 3)),
          XOR2(cut_projection(y, 1), cut_projection(y, 2)),
          XOR3(cut_projection(y, 1), cut_projection(y, 2), cut_projection(y, 3)),
          cut_projection(y, 0),
          XOR2(cut_projection(y, 0), cut_projection(y, 3)),
          XOR2(cut_projection(y, 0), cut_projection(y, 2)),
          XOR3(cut_projection(y, 0), cut_projection(y, 2), cut_projection(y, 3)),
          XOR2(cut_projection(y, 0), cut_projection(y, 1)),
          XOR3(cut_projection(y, 0), cut_projection(y, 2), cut_projection(y, 3)),
          XOR3(cut_projection(y, 0), cut_projection(y, 1), cut_projection(y, 2)),
          XOR4(cut_projection(y, 0), cut_projection(y, 1), cut_projection(y, 2), cut_projection(y, 3)))
    count = 0
    value = 0
    l = None
    size=16
    for index in Rox:
        xor = index[a] ^ index[b]
        l = str(xor)
        for i in l:
            if (i == '1'):
                count += 1
        if ((count/size) % 2 == 1/2):
            value = 0
        else:
            value = int((1 / 2 - count / size)*16)
    #print(index[a], index[b], l)
    return value

lol3 = [int(i) for i in range(0, 30)]

for i in lol3[:15]:
    Possibility[0][i] = test(0,i+15)
for i in lol3[:15]:
    Possibility[1][i] = test(1, i + 15)
for i in lol3[:15]:
    Possibility[2][i] = test(2, i + 15)
for i in lol3[:15]:
    Possibility[3][i] = test(3, i + 15)
for i in lol3[:15]:
    Possibility[4][i] = test(4, i + 15)
for i in lol3[:15]:
    Possibility[5][i] = test(5, i + 15)
for i in lol3[:15]:
    Possibility[6][i] = test(6, i + 15)
for i in lol3[:15]:
    Possibility[7][i] = test(7, i + 15)
for i in lol3[:15]:
    Possibility[8][i] = test(8, i + 15)
for i in lol3[:15]:
    Possibility[9][i] = test(9, i + 15)
for i in lol3[:15]:
    Possibility[10][i] = test(10, i + 15)
for i in lol3[:15]:
    Possibility[11][i] = test(11, i + 15)
for i in lol3[:15]:
    Possibility[12][i] = test(12, i + 15)
for i in lol3[:15]:
    Possibility[13][i] = test(13, i + 15)
for i in lol3[:15]:
    Possibility[14][i] = test(14, i + 15)

print('\n')
for i in Possibility:
    print(i)