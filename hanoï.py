from tkinter import * 

WIDTH_CNV = 900
HEIGHT_CNV = 300

DIST = WIDTH_CNV / 4
BASE = WIDTH_CNV / 4.2
OFFSET = 20
HEIGHT = 40
SEP = 4
SOCLE_LEFT = WIDTH_CNV / 10
SOCLE_RIGHT = 9 * WIDTH_CNV / 10
THICKNESS = 20
TOP = 4 * HEIGHT_CNV / 5
ORIGN = (0, HEIGHT_CNV)

def hanoi(L, source, but, temp, hauteurs, done):
    if L:
        A = hanoi(L[1:], source, temp, but, hauteurs, False)
        B = [(L[0], (source, hauteurs[source] - 1), (but,
                                                     hauteurs[but]))]
        hauteurs[source] -= 1
        hauteurs[but] += 1
        C = hanoi(L[1:], temp, but, source, hauteurs, False)
        if done :
            moves = list(enumerate(A + B + C))
            for (i, (nro, orig, dstn)) in moves:
                cnv.after(1000 * (i + 1), move, nro, orig, dstn)
        return A + B + C
    return []


def move(nro, orig, dstn):
    i, hi = orig
    j, hj = dstn
    dx = (j - i) * DIST
    dy = -(hj - hi) * HEIGHT
    cnv.move(ids[nro], dx, dy)


def chgt(X, Y, center):
    return (X + center[0], -Y + center[1])


root = Tk()

cnv = Canvas(root, width=WIDTH_CNV, height=HEIGHT_CNV, bg="ivory")
cnv.pack()

# Le socle
A = chgt(SOCLE_LEFT, 0, ORIGN)
B = chgt(SOCLE_RIGHT, THICKNESS, ORIGN)
cnv.create_rectangle(A, B, fill="black")

# Les tiges
for i in range(3):
    x = (i + 1) * DIST - THICKNESS / 2
    A = chgt(x, 0, ORIGN)
    B = chgt(x + THICKNESS, TOP, ORIGN)
    cnv.createrectangle(A, B, fill="black")

# Les disques
n = 4
w = BASE
x = DIST - w / 2
y = HEIGHT / 2 + SEP

ids = []

for  in range(n):
    A = chgt(x, y, ORIGN)
    B = chgt(x + w, y + HEIGHT, ORIGN)
    rect = cnv.create_rectangle(A, B, fill="red", outline="")
    ids.append(rect)
    x += OFFSET
    y += HEIGHT + SEP
    w -= 2 * OFFSET


hanoi(list(range(n)), 0, 1, 2, [n, 0, 0], True)

root.mainloop()