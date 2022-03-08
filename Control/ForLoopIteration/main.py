""" ForLoopIteration, código demonstrando o uso do laço for acendendo leds em sequência, depois em reverso 
    autor: Gabriel Zamarioli Youssef
    data: 08/03/2022
"""
from machine import Pin
import time

LEDPINNUM1 = 25 # num do pino do led 1
LEDPINNUM2 = 26 # num do pino do led 2
LEDPINNUM3 = 27 # num do pino do led 3
LEDPINNUM4 = 23 # num do pino do led 4
LEDPINNUM5 = 22 # num do pino do led 5
LEDPINNUM6 = 21 # num do pino do led 6

def loop():
  ledPinVector = [Pin(LEDPINNUM1, Pin.OUT), # vetor com os objetos dos pinos dos leds
                  Pin(LEDPINNUM2, Pin.OUT), 
                  Pin(LEDPINNUM3, Pin.OUT), 
                  Pin(LEDPINNUM4, Pin.OUT), 
                  Pin(LEDPINNUM5, Pin.OUT), 
                  Pin(LEDPINNUM6, Pin.OUT)]
  
  for ledPin in ledPinVector: # vetor em ordem normal
    ledPin.on()
    time.sleep(0.5)
    ledPin.off()

  for ledPin in reversed(ledPinVector): # vetor em ordem inversa
    ledPin.on()
    time.sleep(0.5)
    ledPin.off()

while True:
  loop()