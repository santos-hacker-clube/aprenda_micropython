""" ToneMelody, liga um speaker e faz tocá-lo uma melodia(notas) """

from machine import Pin, PWM
import time

def tone():
  duration = [4,8,8,4,4,4,4,4] # ajuda a calcular o tempo das notas
  notes = [2620, 1960, 1960, 2200, 1960, 1, 2470, 2620] # frequencia das notas
  i = 0
  for x in notes:
    #PWM no pino 25 (buzzer) numa frequência de 4940Hz à 50% de ciclo de trabalho(duty cycle)
    buzzer = PWM(Pin(25), freq=x, duty=512) 
    time.sleep(1/duration[i]) # continua por 500 ms
    buzzer.deinit() # termino
    i += 1
    
while True:
  tone() # execução em sequência