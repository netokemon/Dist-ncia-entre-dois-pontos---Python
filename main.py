import math
ponto1 = input().split(" ")
x1 = float(ponto1[0])
y1 = float(ponto1[1])
ponto2 = input().split(" ")
x2 = float(ponto2[0])
y2 = float(ponto2[1])
distancia = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
print("{:.4f}".format(distancia))