import pgzrun
import random
from random import randint

WIDTH = 1200
HEIGHT = 720
alive = True
gameover = False
score = 0
speed = 4
attack = 1
a = Actor('plane', anchor = ('center', 'center'))
b = Actor('marine', anchor = ('center', 'center'), pos = (1100, 360))
ebul1 = Actor('bulletsilversilver_outline')
ebul2 = Actor('bulletsilversilver_outline')
ebul3 = Actor('bulletsilversilver_outline')
ebul4 = Actor('bulletsilversilver_outline')
ebul5 = Actor('bulletsilversilver_outline')
ebul6 = Actor('bulletsilversilver_outline')
ebul7 = Actor('bulletsilversilver_outline')
ebul8 = Actor('bulletsilversilver_outline')
ebul9 = Actor('bulletsilversilver_outline')
ebul10 = Actor('bulletsilversilver_outline')
ebul11 = Actor('bulletsilversilver_outline')
ebul12 = Actor('bulletsilversilver_outline')
ebul13 = Actor('bulletsilversilver_outline')
ebul14 = Actor('bulletsilversilver_outline')
ebul15 = Actor('bulletsilversilver_outline')
ebul16 = Actor('bulletsilversilver_outline')
ebul17 = Actor('bulletsilversilver_outline')
ebul18 = Actor('bulletsilversilver_outline')
ebul19 = Actor('bulletsilversilver_outline')
ebul20 = Actor('bulletsilversilver_outline')
ebul21 = Actor('bulletsilversilver_outline')
ebul22 = Actor('bulletsilversilver_outline')
ebul23 = Actor('bulletsilversilver_outline')
ebul24 = Actor('bulletsilversilver_outline')
ebuls = [ebul1, ebul2, ebul3, ebul4, ebul5, ebul6, ebul7, ebul8, ebul9, ebul10, ebul11, ebul12]
pb1 = Actor('blue_crystal1')
pb2 = Actor('blue_crystal1')
pbs = [pb1, pb2]
bul = Actor('bulletbluesilver_outline')
H = 6
EH = 60
P = 0
S = False
B = False
upd = 0
bulp = 0
es = 2
eup = 0
ed = 1
ex = random.randint(120, 250)
bs = 0
ebs = 5

for ebul in ebuls:
    ebul.angle = 90
    x = randint(WIDTH, WIDTH*2.5)
    y = randint(0 + ebul.height , HEIGHT - ebul.height)
    ebul.pos = (x,y)
for pb in pbs:
    x = randint(WIDTH, WIDTH*2.5)
    y = randint(0 + pb.height , HEIGHT - pb.height)
    pb.pos = (x,y)
    pb.sh = 1

def ebul1_reset(): ebul_reset(ebul1)
def ebul2_reset(): ebul_reset(ebul2)
def ebul3_reset(): ebul_reset(ebul3)
def ebul4_reset(): ebul_reset(ebul4)
def ebul5_reset(): ebul_reset(ebul5)
def ebul6_reset(): ebul_reset(ebul6)
def ebul7_reset(): ebul_reset(ebul7)
def ebul8_reset(): ebul_reset(ebul8)
def ebul9_reset(): ebul_reset(ebul9)
def ebul10_reset(): ebul_reset(ebul10)
def ebul11_reset(): ebul_reset(ebul11)
def ebul12_reset(): ebul_reset(ebul12)
def ebul13_reset(): ebul_reset(ebul1)
def ebul14_reset(): ebul_reset(ebul2)
def ebul15_reset(): ebul_reset(ebul3)
def ebul16_reset(): ebul_reset(ebul4)
def ebul17_reset(): ebul_reset(ebul5)
def ebul18_reset(): ebul_reset(ebul6)
def ebul19_reset(): ebul_reset(ebul7)
def ebul20_reset(): ebul_reset(ebul8)
def ebul21_reset(): ebul_reset(ebul9)
def ebul22_reset(): ebul_reset(ebul10)
def ebul23_reset(): ebul_reset(ebul11)
def ebul24_reset(): ebul_reset(ebul12)

def pb1_reset(): pb_reset(pb1)
def pb2_reset(): pb_reset(pb2)

def ebul_reset(ebul):
    x = randint(WIDTH, WIDTH*2)
    y = randint(0 , HEIGHT)
    ebul.pos = (x,y)

def pb_reset(pb):
    x = randint(WIDTH, WIDTH*2)
    y = randint(0 , HEIGHT)
    pb.pos = (x,y)

def bul_reset():
    global bulp
    bulp = 2
    clock.schedule_unique(bul_rreset, 0.2)
    
def bul_rreset():
    global bulp
    bulp = 0

def speed_up():
    global speed
    global P
    global S
    S = True
    speed = 7
    P -= 2

def up_bullet():
    global P
    global B
    global attack
    attack = 3
    bul.image = 'bulletredsilver_outline'
    P -= 2
    B = True
    
def upenemy():
    global es
    global eup
    global ebs
    es = 5
    b.image = 'marinex'
    ebs = 7
    ebuls.append(ebul13)
    ebuls.append(ebul14)
    ebuls.append(ebul15)
    ebuls.append(ebul16)
    ebuls.append(ebul17)
    ebuls.append(ebul18)
    ebuls.append(ebul19)
    ebuls.append(ebul20)
    ebuls.append(ebul21)
    ebuls.append(ebul22)
    ebuls.append(ebul23)
    ebuls.append(ebul24)
    for ebul in ebuls:
        ebul.angle = 90
        x = randint(WIDTH, WIDTH*2.5)
        y = randint(0 + ebul.height , HEIGHT - ebul.height)
        ebul.pos = (x,y)
    eup = 0

def update():
    global H
    global alive
    global gameover
    global speed
    global P
    global S
    global B
    global upd
    global bul
    global EH
    global bulp
    global es
    global eup
    global ex
    global ed
    global bs
    global score
    global ebs
    
    if alive:
        if P >= 2:
            upd = 1
            a.image = 'update'
        else:
            upd = 0
            a.image = 'plane'
        if keyboard.left and a.x > 0:
            a.x -= speed
        if keyboard.right and a.x < WIDTH:
            a.x += speed
        if keyboard.up and a.y > 0:
            a.y -= speed
        if keyboard.down and a.y < HEIGHT:
            a.y += speed
      #  if up == True:
        if keyboard.s and upd == 1:
            if not S:
                speed_up()
        if keyboard.b and upd == 1:
            if not B:
                up_bullet()
        if keyboard.h and upd == 1:
            H += 2
            P -= 2
        if eup == 1:
            upenemy()
        for ebul in ebuls:
            ebul.x -= ebs
            if ebul.colliderect(a):
                H -= 1
                bs += 1
                ebul_reset(ebul)
                if H == 0:
                    a.image = 'explode'
                    alive = False
            if ebul.x < 0:
                    ebul_reset(ebul)
        for pb in pbs:
            pb.x -= 5
            if pb.colliderect(a):
                P += 1
                pb_reset(pb)
            if pb.x < 0:
                    pb_reset(pb)
        if bulp == 0:
            if keyboard.space:
                bulp = 1
                bul.angle =270
                bul.pos = a.pos
                bul.x += 15
        if bulp == 1:
            bul.x += 15
            if bul.colliderect(b):
                EH -= 1
                bul_reset()
                if EH == 30:
                    eup = 1
                if EH == 0:
                    b.image = 'explode'
                    alive = False
            if bul.x > WIDTH:
                    bul_reset()
        b.y += es*ed
        if b.y == HEIGHT/2 + ex:
            ed = ed * (-1)
            ex = random.randint(-240, 240)
        elif b.y <= 0 or b.y >= HEIGHT:
            ed = ed* (-1)
    else:
        gameover = True
        score = 60-EH - bs
        if score < 0:
            score = 0

def draw():
    screen.blit('background', (0, 0))
    screen.draw.text("Health: " + str(H), (20, 20), color="orange", fontsize=30)
    if gameover:
        screen.draw.text("Your score: " + str(score), (480, 340), color="green", fontsize=50)
    a.draw()
    b.draw()
    
    for ebul in ebuls:
        ebul.draw()
    for pb in pbs:
        pb.draw()
    if bulp == 1:
        bul.draw()