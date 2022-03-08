""" Este código exemplifica o uso do while em python 
    autor: Gabriel Zamarioli Youssef
    data: 08/03/2022
"""
from machine import Pin, ADC, PWM
import time
SENSORPINNUM = 35 # pino do fotosensor
SWITCHBTPINNUM = 26 # pino do switch
BUILTINLEDPINNUM = 2 # pino do led interno
LEDPINNUM = 25 # pino do led externo

def loop():
  builtinLedPin = Pin(BUILTINLEDPINNUM, Pin.OUT) # objeto do pino do led interno
  ledPin = Pin(LEDPINNUM, Pin.OUT) # objeto do pino do led externo
  sensorPin =  Pin(SENSORPINNUM, Pin.IN) # objeto do pino do fotosensor
  adcSensorPin = ADC(sensorPin) # objeto ADC do forosensor
  switcBtnPin = Pin(SWITCHBTPINNUM, Pin.IN) # objeto do pino do switch
  while switcBtnPin.value() == 1: # enquanto o botão do switch estiver ligado, calibragem
    calibrate()
  builtinLedPin.off() # desliga o led interno, calibragem terminou
  sensorValue = adcSensorPin.read() # leitura do fotosensor
  sensorValue = int((sensorValue / 4063) * 1023) # adequando o valor para usar no led(1-1023)
  pwm = PWM(ledPin, freq=5000, duty=sensorValue) # objeto PWM do led
  pwm.deinit() # desliga
  return


def calibrate():
  sensorMax = 32 # valor maximo usado na calibragem
  sensorMin = 4063 # valor minimo usado na calibragem
  builtinLedPin = Pin(BUILTINLEDPINNUM, Pin.OUT) # objeto do pino do led interno #2
  sensorPin =  Pin(SENSORPINNUM, Pin.IN) # objeto do pino do fotosensor #2
  adcSensorPin = ADC(sensorPin) # objeto ADC do fotosensor #2
  builtinLedPin.on() # ligado, indica o começo da calibragem
  value = adcSensorPin.read() # leitura do sensor, calibragem
  if (value > sensorMax):
    sensorMax = value
  if (value < sensorMin):
    sensorMin = value

while True:
  loop()