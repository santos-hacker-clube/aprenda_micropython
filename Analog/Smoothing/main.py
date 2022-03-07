""" Smoothing
    Leituras analógicas sucessivas do pino 35,
    guardando no vetor leituras. Calculando a média dos valores
    (smoothing) e mostrando na tela
    Gabriel Zamarioli Youssef
    data: 07/03/2022
"""

from machine import Pin, ADC
import time

NUMPINENTRADA = 35 # numero do pin de entrada
NUMSLEITURAS = 10 # quantidade de leituras (quando mais, mais suaviazado fica)
total = 0 # usado no calculo de smoothing
leituras = [0] * NUMSLEITURAS # vetor para guarda as leituras
indexLeitura = 0 # indice do vetor

def loop():
  global total, leituras, indexLeitura
  inPin = Pin(NUMPINENTRADA, Pin.IN) # objeto do pino de entrada
  AdcInPin = ADC(inPin) # objeto ADC do pino de entrada
  total = total - leituras[indexLeitura] # apaga a ultima entrada
  leituras[indexLeitura] = AdcInPin.read() # leitura da entrada
  total = total + leituras[indexLeitura] # guarda o valor no vetor
  indexLeitura += 1 # indexLeitura++
  if indexLeitura >= NUMSLEITURAS: # caso o vetor fique cheio
    indexLeitura = 0
  media = total / NUMSLEITURAS # média do vetor
  print(media)
  time.sleep(0.5) # velocidade de preenchimento

while True:
  loop()