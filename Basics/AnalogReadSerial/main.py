'''
Realiza a leitura de uma entrada analógica no pino 35,
exibe no shell e varia o seu valor utilizando um potenciometro (0-4095).
'''

from machine import Pin, ADC
import time

def AnalogReadSerial():
    adc = ADC(Pin(35, Pin.IN)) #cria um objeto ADC atuando no pino 35
    val = adc.read() #lê uma entrada no pino analógico 35
    print(val) #imprime o valor no Shell

while(True): #loop
    AnalogReadSerial() #chamada da função
    time.sleep(0.5) #descanso de 500ms entre as entradas