import math

xA = float(input('Abscissa do ponto A:'))
xB = float(input('Abscissa do ponto B:'))

yA = float(input('Ordenada do ponto A:'))
yB = float(input('Abscissa do ponto B:'))


distance = math.sqrt((xA-xB)**2) + ((yA-yB)**2)

if distance >= 10:
    print('longe')
else:
    print('perto')
