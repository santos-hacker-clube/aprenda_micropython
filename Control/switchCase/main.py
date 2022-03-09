""" Este código implementa uma alternativa ao switch case do C++, usando dicionário 
    autor: Gabriel Zamarioli Youssef
    data: 08/03/2022
"""

from machine import Pin, ADC
import time, math

PINNUM = 35 # numero do pino usado

def loop():
  inPin = Pin(PINNUM, Pin.IN) # objeto do pino 35
  adcPin = ADC(inPin) # objeto ADC do pino 35
  value = math.floor((adcPin.read() / 4063) * 3) # conversão do valor de entrada para um número [0,3]
  dic = { 3 : 'dark', 2: 'dim', 1 : 'medium', 0 : 'bright'} # nível de claridade
  print(dic[value]);
  time.sleep(1)

while True:
  loop()
