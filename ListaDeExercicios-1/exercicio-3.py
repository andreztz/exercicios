total_segs = int(input('Por favor, entre com o número de segundos que deseja converter: '))

dias  = total_segs // 86400
temp_restante = total_segs % 86400

total_segs = temp_restante
horas = total_segs // 3600

segs_restantes = total_segs % 3600
minutos = segs_restantes // 60
segs_restantes_final = segs_restantes % 60

segundos = segs_restantes_final % 60

print("{} dias, {} horas, {} minutos e {} segundos.".format(dias, horas, minutos, segundos))
