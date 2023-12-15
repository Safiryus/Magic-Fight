import pgzrun
from kivy.clock import Clock
from pgzero.builtins import Actor, animate, keyboard
import os
os.environ['SDL_VIDEO_CENTERED'] = '1'
g = Actor("göz")
eg = 10
ey = 10
WIDTH = g.width*eg
HEIGHT = g.height*ey
zaman1 = 3
zaman2 = 3
zamans1 = 3
zamans2 = 3
fler = []
ae2 = True
fler2 = []
kz1 = Actor("kazanan1")
kz2 = Actor("kazanan2")
grs = Actor("giriş")
tnt = Actor("tanıtım")
ty = Actor("tol", (WIDTH/2, 400))
oy = Actor("ool", (WIDTH/2, HEIGHT/2 + 50))
o1 = Actor("aw" )
o2 = Actor("o2tekka")
k = Actor("kalkan1", (5*g.width, 5*g.height))
b = Actor("bary")
b2 = Actor("bary")
akp = Actor("akp")
tko = Actor("tko", (500, 500))
aen1 = True
aen2 = True
def skin():
    o1.image = "aw"
def skin2():
    o2.image = "o2tekka"
FPS = 60
mod = "giriş"
md1 = 6
def mdr1():
    md1 += 2
    mod = "oyun"
md2 = 6
def mdr2():
    md2 += 2
    mod = "oyun"
kler = []
canlar = []
ex = 0
eh = 0
modk = "o0"
mc1 = True
mc2 = True
ae= True
cg = False
aed = True
ksy = 0
csr = 0
haritam = [[11, 0, 0, 0, 0, 0, 0, 0, 0, 8,],
            [0, 1, 1, 1, 1, 1, 1, 1, 1, 0],
            [0, 1, 1, 1, 1, 1, 1, 1, 1, 0],
            [0, 1, 1, 1, 1, 1, 1, 1, 1, 0],
            [0, 1, 1, 1, 0, 0, 1, 1, 1, 0],
            [0, 1, 1, 1, 0, 0, 1, 1, 1, 0],
            [0, 1, 1, 1, 1, 1, 1, 1, 1, 0],
            [0, 1, 1, 1, 1, 1, 1, 1, 1, 0],
            [0, 1, 1, 1, 1, 1, 1, 1, 1, 0],
            [10, 0, 0, 0, 0, 0, 0, 0, 0, 9]]
            
o1.y = 1.5*g.height
o1.x = 1.5*g.width
o1.h = 300
#oyuncu 2
 
o2.y = 8.5*g.height
o2.x = 8.5*g.width
o2.h = 300
ka = True
#can
def draw():
    global WIDTH
    global HEIGHT
    if mod =="giriş":
        grs.draw()
        ty.draw()
    if mod == "tanıtım":
        tnt.draw()
        oy.draw()
    if mod == "oyun":
        WIDTH = g.width*eg
        HEIGHT = g.height*ey
        akp.draw()
        hc()
        for i in canlar:
            if cg == True:
                i.draw()
        b.draw()
        b2.draw()
        o1.draw()
        o2.draw()
        if ka == True:
            k.draw()
        for i in fler:
            if ae == True:
                i.draw()
        for i in fler2:
            if ae2 == True:
                i.draw()
    if mod == "kazanan1":
        WIDTH = kz1.width
        HEIGHT = kz1.height       
        kz1.draw()
        tko.draw()
    if mod == "kazanan2":
        WIDTH = kz2.width
        HEIGHT = kz2.height
        kz2.draw()
        tko.draw()
    if mod == "oyun":
        WIDTH = g.width*eg
        HEIGHT = g.height*ey
        akp.draw()
        hc()
        for i in canlar:
            if cg == True:
                i.draw()
        b.draw()
        b2.draw()
        o1.draw()
        o2.draw()
        if ka == True:
            k.draw()
        for i in fler:
            if ae == True:
                i.draw()
        for i in fler2:
            if ae2 == True:
                i.draw()
            
def hc():
    global WIDTH
    global HEIGHT
    for i in range(len(haritam)):
        for j in range(len(haritam[0])):
            g.left = g.width*j
            g.top = g.height*i
            if haritam[i][j] == 0:
                g.image = "göz"
                g.draw()
            if haritam[i][j] == 8:
                g.image = "kose"
                g.draw()
            if haritam[i][j] == 9:
                g.image = "kose2"
                g.draw()    
            if haritam[i][j] == 10:
                g.image = "kose3"
                g.draw()
            if haritam[i][j] == 11:
                g.image = "kosew"
                g.draw()    
            if haritam[i][j] == 1:
                g.image = "yol1"
                g.draw()      

def update(dt):
    global zaman1
    global zaman2
    global zamans1 
    global zamans2 
    global WIDTH
    global HEIGHT
    global ex
    global ey
    global ka
    global modk
    global ksy
    global mod
    global md1
    global md2
    global mc1
    global mc2
    global ae
    global ile
    global cg
    global ae2
    b.x = o1.x
    b.y = o1.y - 0.25*g.height
    b2.x = o2.x
    b2.y = o2.y - 0.25*g.height
    #o2 hareket
    if o2.x + g.width < WIDTH - 0.5*g.width and keyboard.right:
        o2.x += 0.05*g.width
        ex = o2.x
        eh = o2.y
    if keyboard.left and o2.x - 0.5*g.width > g.width:
        o2.x -= 0.05*g.width
        ex = o2.x
        eh = o2.y
    if keyboard.up and o2.y > g.height:
        o2.y -= 0.05*g.height
        ex = o2.x
        eh = o2.y
    if keyboard.down and o2.y < HEIGHT - 1.5*g.height:
        o2.y += 0.05*g.height
        ex = o2.x
        eh = o2.y
    #o1 hareket
    if o1.x + g.width < WIDTH - 0.5*g.width and keyboard.d:
        o1.x += 0.05*g.width
        ex = o1.x
        eh = o1.y
    if keyboard.a and o1.x - 0.5*g.width > g.width:
        o1.x -= 0.05*g.width
        ex = o1.x
        eh = o1.y
    if keyboard.w and o1.y > g.height:
        o1.y -= 0.05*g.height
        ex = o1.x
        eh = o1.y
    if keyboard.s and o1.y < HEIGHT - 1.5*g.height:
        o1.y += 0.05*g.height
        ex = o1.x
        eh = o1.y
    for i in fler:
        if i.direction == "a":
            i.x -= 6.5
        if i.direction == "d":
            i.x += 6.5
        if i.direction == "w":
            i.y -= 6.5
        if i.direction == "s":
            i.y += 6.5
    for i in fler2:
        if i.direction == "left":
            i.x -= 6.5
        if i.direction == "right":
            i.x += 6.5
        if i.direction == "up":
            i.y -= 6.5
        if i.direction == "down":
            i.y += 6.5
    if o1.colliderect(k):
        modk = "o1"
        ka = False
    if mod == "oyun" and modk == "o1":
        ae = True
    if keyboard.z and mod == "oyun" and modk == "o1":
        ka = True
        mc1 = False
        ae = False
        k.pos = o1.pos
        ksy += 1
    #o2 kalkansız ama kalkanlı
    if keyboard.x and mod == "oyun" and modk == "o2":
        mc2 = True
    if mod == "oyun" and modk == "o2":
        mc2 = True
    #o1 kalkansız ama kalkanlı
    if keyboard.rctrl and mod == "oyun" and modk == "o1":
        mc1 = True
    if mod == "oyun" and modk == "o1":
        mc1 = True
    #o2 korunma
    if keyboard.x and mod == "oyun" and modk == "o2" and keyboard.rshift:
        mc2 = False
    if mod == "oyun" and modk == "o2" and keyboard.rctrl:
        mc2 = False
    #o1 koruma
    if keyboard.rctrl and mod == "oyun" and modk == "o1" and keyboard.z:
        mc1 = False
    if mod == "oyun" and modk == "o1" and keyboard.z:
        mc1 = False
    if ksy == 310 and modk == "o1":
        k.x = 5*g.width
        k.y = 5*g.height
        modk = "o0"
        ksy = 0
        ka = True
        ae = True
        mc1 = True
    #o2 kalkan
    if o2.colliderect(k):
        modk = "o2"
        ka = False
    if mod == "oyun" and modk == "o2":
        ae2 = True
    if keyboard.rshift and mod == "oyun" and modk == "o2":
        ka = True
        mc2 == False
        ae2 = False
        k.pos = o2.pos
        ksy += 1
    if ksy == 310 and modk == "o2":
        k.x = 5*g.width
        k.y = 5*g.height
        modk = "o0"
        ksy = 0
        ka = True
        ae2 = True
        mc2 = True
    #o1 hasar alma
    for i in fler2:
        if o1.colliderect(i) and mc1 == True:
            o1.h -= 0.55
        if o1.h >= 200 and o1.h < 250:
            b.image = "bars"
        if 100 <= o1.h and o1.h < 200:
            b.image = "bart"
        if 0 < o1.h and o1.h < 100:
            b.image = "bark"
        if o1.h <= 0:
            mod = "kazanan2"
    #o2 hasar alma
    for i in fler:
        if o2.colliderect(i) and mc2 == True:
            o2.h -= 0.55
        if 200 <= o2.h and o2.h < 250:
            b2.image = "bars"
        if 100 <= o2.h and o2.h < 200:
            b2.image = "bart"
        if 0 < o2.h and o2.h < 100:
            b2.image = "bark"
        if o2.h <= 0:
            mod = "kazanan1"

                


def on_key_down(key):
    global WIDTH
    global HEIGHT
    global mod
    global md1
    global ka
    global zaman1
    global zaman2
    global zamans1
    global zamans2
    global md2
    global ksy
    global modk
    global b
    global b2
    if (mod == "kazanan1" or mod == "kazanan2" or mod == "tanıtım") and keyboard.space:
        mod = "oyun"
        o1.h = 300
        o2.h = 300
        b.image = "bary"
        b2.image = "bary"
        k.x = g.width*5
        k.y = g.height*5
        ka = True
        modk = "o0"
        o1.y = 1.5*g.height
        o1.x = 1.5*g.width
        o2.y = 8.5*g.height
        o2.x = 8.5*g.width
        ae = True
        ae2 = True 
        mc1 = True
        mc2 = True
    if mod == "tanıtım" and keyboard.space:
        mod = "oyun"
    if mod == "giriş" and keyboard.space:
        mod = "tanıtım"
    if keyboard.x and (mod == "oyun" or mod == "oyunmd2") and keyboard.d:
        o1.image = "qp"
        f = Actor("awer")
        f.direction = "d"
        f.pos = o1.pos
        fler.append(f)
        md1 -= 1
        Clock.schedule_interval(lambda dt: skin(), 2.5)
    if keyboard.x and (mod == "oyun" or mod == "oyunmd2") and keyboard.a:
        o1.image = "qp"
        f = Actor("awer")
        f.direction = "a"
        f.pos = o1.pos
        fler.append(f)
        md1 -= 1
        Clock.schedule_interval(lambda dt: skin(), 2.5)
    if keyboard.x and (mod == "oyun" or mod == "oyunmd2") and keyboard.w:
        o1.image = "qp"
        f = Actor("awer")
        f.direction = "w"
        f.pos = o1.pos
        fler.append(f)
        md1 -= 1
        Clock.schedule_interval(lambda dt: skin(), 2.5)
    if keyboard.x and (mod == "oyun" or mod == "oyunmd2") and keyboard.s:
        o1.image = "qp"
        f = Actor("awer")
        f.direction = "s"
        f.pos = o1.pos
        fler.append(f)
        md1 -= 1
        
    #o2 ateş 
    if keyboard.rctrl and (mod == "oyun" or mod == "oyunmd1") and keyboard.right:
        o2.image = "maygat"
        f2 = Actor("atrigga2")
        f2.direction = "right"
        f2.pos = o2.pos
        fler2.append(f2)
        md2 -= 1
        Clock.schedule_interval(lambda dt: skin2(), 2.5)
    if keyboard.rctrl and (mod == "oyun" or mod == "oyunmd1") and keyboard.left:
        o2.image = "maygat"
        f2 = Actor("atrigga2")
        f2.direction = "left"
        f2.pos = o2.pos
        fler2.append(f2)
        md2 -= 1
        Clock.schedule_interval(lambda dt: skin2(), 2.5)
    if keyboard.rctrl and (mod == "oyun" or mod == "oyunmd1") and keyboard.up:
        o2.image = "maygat"
        f2 = Actor("atrigga2")
        f2.direction = "up"
        f2.pos = o2.pos
        fler2.append(f2)
        md2 -= 1
        Clock.schedule_interval(lambda dt: skin2(), 2.5)
    if keyboard.rctrl and (mod == "oyun" or mod == "oyunmd1") and keyboard.down:
        o2.image = "maygat"
        f2 = Actor("atrigga2")
        f2.direction = "down"
        f2.pos = o2.pos
        fler2.append(f2)
        md2 -= 1
        Clock.schedule_interval(lambda dt: skin2(), 2.5)       

pgzrun.go()