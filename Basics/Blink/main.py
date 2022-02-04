'''
Liga e desliga o Led Interno de um Nodemcu (ESP32 ou ESP8266)
por meio segundo repetidamente.
'''

from machine import Pin
from time import sleep

#cria o objeto led que usa o pino 2 (led interno) como saída
led = Pin(2, Pin.OUT)

#executa o loop infinito modificando o valor de led
while True:
    led.value(not led.value()) #altera o valor do led
    sleep(0.5) #aguarda meio segundo
    
#para interromper a execução basta pressional CTRL+C no Shell