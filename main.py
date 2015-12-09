import Vlibrary
from Vlibrary import *

#2D products.
print("2D Vectors A and B: ")
A = Vec2(5,9)
B = Vec2(3,7)
C = Vec2(0,0)
D = Vec2(0,0)
E = Vec2(0,0)
F = Vec2(0,0)

print (A.x, A.y)
print (B.x, B.y)
print

print("addition2:")
C = A.add2D(B)
print(C.x, C.y)
print

print("subtration2:")
C = A.sub2D(B)
print (C.x, C.y)
print

print("magnitude2:")
C = A.mag2(A)
D = B.mag2(B)
print(C)
print(D)
print

print("normalisation2:")
C = A.nor2x(A)
D = A.nor2y(A)
E = B.nor2x(B)
F = B.nor2y(B)
print(C)
print(D)
print(E)
print(F)
print

print("dot2:")
C = A.multi2D(B)
print (C)
print

print("linear2:")
C = A.lin2D(B)
print(C.x, C.y)
print
print


#3D products.
print("3D Vectors G and H: ")
G = Vec3(6,2,4)
H = Vec3(7,5,1)
I = Vec3(0,0,0)
J = Vec3(0,0,0)
K = Vec3(0,0,0)
L = Vec3(0,0,0)
M = Vec3(0,0,0)
N = Vec3(0,0,0)

print(G.x, G.y)
print(H.x, H.y)
print


print("addition3:")
I = G.add3D(H)
print(I.x, I.y, I.z)
print

print("subtration3:")
I = G.sub3D(H)
print(I.x, I.y, I.z)
print

print("magnitude3:")
I = G.mag3(G)
J = H.mag3(H)
print(I)
print(J)
print

print("normalisation3:")
I = G.nor3x(G)
J = G.nor3y(G)
K = G.nor3z(G)
L = H.nor3x(H)
M = H.nor3y(H)
N = H.nor3z(H)
print"g.x:",I
print"g.y:",J
print"g.z:",K
print"h.x:",L
print"h.y:",M
print"h.z:",N
print

print("dot3:")
I = G.multi3D(H)
print (I)
print

print("linear3:")
I = G.lin3D(H)
print(I.x, I.y, I.z)
print

print("cross:")
I = G.cross3D(H)
print(I)

