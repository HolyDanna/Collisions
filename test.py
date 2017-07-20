from elements.AABB import AABB
from elements.OBB import OBB
from elements.Circle import Circle
from elements.Polygon import Polygon
from elements.Point import Point
from Game.collisions import *

a1 = AABB(100,100,100,100)
a2 = AABB(200,100,100,100)
a3 = AABB(210,210,100,100)
a4 = AABB(120,120,60,60)
a5 = AABB(120,120,100,200)
a = [a1,a2,a3,a4,a5]

i=0
if i:
    print("Test for AABB elements")
    print()
    print("Elements a1 has a common side with element a2")
    print("Elements a3 does not touch element a1, a2 and a4")
    print("Element a4 is inside element a1, but does not cross one of its side")
    print("Element a5 cross all 4 other elements")
    for x in range(len(a)):
        for y in range(len(a)):
            if x is not y:
                # print("Intersection of element a"+str(x+1)+" and element a"+str(y+1))
                print("a"+str(x+1)+"/a"+str(y+1)+" "+str(checkCollisions(a[x],[a[y]], False)))
                # print(checkCollisions(a[x],[a[y]], False)==checkCollisions(a[y],[a[x]], False))

else:
    print("The AABB a4 is in AABB a1. Collision check : a1/a4 "+str(checkCollisions(a[0],[a[3]], False))+" a4/a1 "+str(checkCollisions(a[3],[a[0]], False)))
    print("The AABB a1 and AABB a2 shares a side. Collision check : a1/a2 "+str(checkCollisions(a[0],[a[1]], False))+" a2/a1 "+str(checkCollisions(a[1],[a[0]], False)))
    print("The AABB a3 does not touch a1, a2 or a4. Collision check : a3/a1 "+str(checkCollisions(a[2],[a[0]], False))+" a1/a3 "+str(checkCollisions(a[0],[a[2]], False)))
    print("Collision check : a3/a2 "+str(checkCollisions(a[2],[a[1]], False))+" a2/a3 "+str(checkCollisions(a[1],[a[2]], False)))
    print("Collision check : a3/a4 "+str(checkCollisions(a[2],[a[3]], False))+" a4/a3 "+str(checkCollisions(a[3],[a[2]], False)))
    print("The AABB a5 touches all the others. Collision check : a5/a1 "+str(checkCollisions(a[4],[a[0]], False))+" a1/a5 "+str(checkCollisions(a[0],[a[4]], False)))
    print("Collision check : a5/a2 "+str(checkCollisions(a[4],[a[1]], False))+" a2/a5 "+str(checkCollisions(a[1],[a[4]], False)))
    print("Collision check : a5/a3 "+str(checkCollisions(a[4],[a[2]], False))+" a3/a5 "+str(checkCollisions(a[2],[a[4]], False)))
    print("Collision check : a5/a4 "+str(checkCollisions(a[4],[a[3]], False))+" a4/a5 "+str(checkCollisions(a[3],[a[4]], False)))

b1 = OBB(100,100,[100,100],[-100,100])
b2 = OBB(200,100,[25,10],[4,-10])
b3 = OBB(200,200,[100,0],[0,100])
b4 = OBB(100,200,[100,200],[-100,50])
b5 = OBB(80,80,[338, 169], [-80, 160])
b = [b1, b2, b3, b4, b5]

if i:
    print("Test for OBB elements, including collision with AABB elements")
    for x in range(len(b)):
        for y in range(len(b)):
            if x is not y:
                # print("Intersection of element a"+str(x+1)+" and element a"+str(y+1))
                print("b"+str(x+1)+"/b"+str(y+1)+" "+str(checkCollisions(b[x],[b[y]], False)))
    for x in range(len(b)):
        for y in range(len(a)):
            # print("Intersection of element a"+str(x+1)+" and element a"+str(y+1))
            print("b"+str(x+1)+"/a"+str(y+1)+" "+str(checkCollisions(b[x],[a[y]], False)))
            # print(checkCollisions(b[x],[a[y]], False) == checkCollisions(a[y],[b[x]], False))
else:
    print("les OBB b1 et b2 ne se touchent pas. Collision check : b1/b2 "+str(checkCollisions(b[0],[b[1]], False))+" b2/b1 "+str(checkCollisions(b[1],[b[0]], False)))
    print("les OBB b1 et b3 ont un coin en commun. Collision check : b1/b3 "+str(checkCollisions(b[0],[b[2]], False))+" b3/b1 "+str(checkCollisions(b[2],[b[0]], False)))
    print("l'OBB b4 sort de l'OBB b1. Collision check : b4/b1 "+str(checkCollisions(b[3],[b[0]], False))+" b1/b4 "+str(checkCollisions(b[0],[b[3]], False)))
    print("l'OBB b1 est en contact avec l'AABB a1. Collision check : b1/a1 "+str(checkCollisions(b[0],[a[0]], False))+" a1/b1 "+str(checkCollisions(a[0],[b[0]], False)))
    print("l'OBB b2 n'est pas en contact avec l'AABB a3. Collision check : b2/a3 "+str(checkCollisions(b[1],[a[2]], False))+" a3/b2 "+str(checkCollisions(a[2],[b[1]], False)))


c1 = Circle(200,200,50)
c2 = Circle(300,200,60)
c3 = Circle(200,300,30)
c4 = Circle(200,200,20)
c5 = Circle(200,200,200)
c = [c1, c2, c3, c4, c5]

if i:
    print("Test for Circle, including collision with AABB or OBB elements")
    for x in range(len(c)):
        for y in range(len(c)):
            if x is not y:
                # print("Intersection of element a"+str(x+1)+" and element a"+str(y+1))
                print("c"+str(x+1)+"/c"+str(y+1)+" "+str(checkCollisions(c[x],[c[y]], False)))
    for x in range(len(c)):
        for y in range(len(b)):
            if x is not y:
                # print("Intersection of element a"+str(x+1)+" and element a"+str(y+1))
                print("c"+str(x+1)+"/b"+str(y+1)+" "+str(checkCollisions(c[x],[b[y]], False)))
    for x in range(len(c)):
        for y in range(len(a)):
            # print("Intersection of element a"+str(x+1)+" and element a"+str(y+1))
            print("c"+str(x+1)+"/a"+str(y+1)+" "+str(checkCollisions(c[x],[a[y]], False)))
            # print(checkCollisions(b[x],[a[y]], False) == checkCollisions(a[y],[b[x]], False))
else:
    print("Le cercle c4 et le cercle c2 ne se touchent pas. Collision check : c2/c4 "+str(checkCollisions(c[1],[c[3]], False))+" c4/c2 "+str(checkCollisions(c[3],[c[1]], False)))
    print("Le cercle c4 est dans le cercle c1. Collision check : c4/c1 "+str(checkCollisions(c[3],[c[0]], False))+" c1/c4 "+str(checkCollisions(c[0],[c[3]], False)))
    print("Le cercle c1 et le cercle c2 se touchent. Collision check : c1/c2 "+str(checkCollisions(c[0],[c[1]], False))+" c2/c1 "+str(checkCollisions(c[1],[c[0]], False)))
    print("Le cercle c1 et l'OBB b2 ne se touchent pas. Collision check : c1/b2 "+str(checkCollisions(c[0],[b[1]], False))+" b2/c1 "+str(checkCollisions(b[1],[c[0]], False)))
