"""  ReadAnalogVoltage_ESP32 lê uma entrada analógica no pino 35
   e mostra no Shell o valor """

from machine import Pin, ADC # importando as bibliotecas(funções) necessárias
import time

def ReadAnalogVoltage_ESP32():
    adc = ADC(Pin(35, Pin.IN)) # cria um objeto ADC atuando no pino 35
    adc.atten(adc.ATTN_11DB) # atenuação
    val = adc.read() # lê uma entrada no pino analógico 35
    val *= (3.3 / 4095) # converte uma entrada analógica (0-4095)
                        # em uma tensão(0-3.3V)
    print(val) # imprime o valor no Shell

while(True): # loop
    ReadAnalogVoltage_ESP32() # chamada da função
    time.sleep(0.5) # descanso entre as entradas
