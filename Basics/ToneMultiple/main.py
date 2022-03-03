""" ToneMultiple, multiplos speakers trabalhando em sequência, em diferentes frequências """

from machine import Pin, PWM
import time

def tone():
  #PWM no pino 26 (buzzer 1) numa frequência de 4400Hz à 50% de ciclo de trabalho(duty cycle)
  buzzer1 = PWM(Pin(26), freq=4400, duty=512) 
  time.sleep(0.2) # continua por 200 ms
  buzzer1.deinit() # termino
  #PWM no pino 25 (buzzer 2) numa frequência de 4940Hz à 50% de ciclo de trabalho(duty cycle)
  buzzer2 = PWM(Pin(25), freq=4940, duty=512) 
  time.sleep(0.5) # continua por 500 ms
  buzzer2.deinit() # termino
  #PWM no pino 21 (buzzer 3) numa frequência de 5230 à 50% de ciclo de trabalho(duty cycle)
  buzzer3 = PWM(Pin(21), freq=5230, duty=512) 
  time.sleep(0.3) # continua port 300 ms
  buzzer3.deinit() # termino
  
while True:
  tone() # execução em sequência
