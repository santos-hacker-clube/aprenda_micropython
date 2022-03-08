""" Código demonstrando o uso do if/else, caso o valor lido pelo potenciometro ultrapasse
    o valor limite estabelecido, liga-se o led, e desliga caso contrário(else)
   autor: Gabriel Zamarioli Youssef
   data: 08/03/2022 
"""


from machine import Pin, ADC
import time

LEDPINNUM = 25 # pino do led
POTPINUM = 35 # pino do potenciometro


def loop():
  limite = 2000
  ledPin = Pin(LEDPINNUM, Pin.OUT) # objeto do pino do led
  potPin = Pin(POTPINUM, Pin.IN) # objeto do pino do potenciometro
  adcPin = ADC(potPin) # objeto ADC do pino 35
  valor = adcPin.read() # leitura
  if valor > limite: # caso o valor ultrapasse o treshold
    ledPin.on() # liga
  else:
    ledPin.off() # desliga
  print(valor)
  time.sleep(0.5) # tempo entre leituras, para estabilidade
  return

while True:
  loop()