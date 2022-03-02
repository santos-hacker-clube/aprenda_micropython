""" Calibration usa um fotosensor no pino 32 para variar a intensidade do led
    no pino 25, préviamente calibrado por 5 segundos indicado pelo led da placa
    (GPIO2)
"""
from machine import Pin, ADC, PWM
import time

sensor_pin = Pin(34, Pin.IN) # pino do foto sensor
sensor_pin = ADC(sensor_pin) # obejto adc do pino
sensorMax = 32 # valor inicial máximo
sensorMin = 4063 # valor inicial mínimo

def setup():
  start = time.ticks_ms() # contagem inicial do tempo de calibragem
  inbuilt_led = Pin(2, Pin.OUT) 
  inbuilt_led.on() # led da placa indica o início
  delta = time.ticks_diff(time.ticks_ms(), start)
  global sensorMax, sensorMin, sensor_pin
  while delta < 5000: # 5 segundos de calibragem
    sensorValue = sensor_pin.read() # leitura do foto sensor
    if sensorValue > sensorMax: # calibragem
      sensorMax = sensorValue
    if sensorValue < sensorMin: # idem
      sensorMin = sensorValue
    delta = time.ticks_diff(time.ticks_ms(), start)
  inbuilt_led.off() # fim da calibragem

setup()

while True:
  sensorValue = sensor_pin.read()
  if sensorValue < sensorMin: # usando os dados da calibragem
    sensorValue = sensorMin
  if sensorValue > sensorMax:
    sensorValue = sensorMax
  frequencia = 5000 # frequencia do led
  led = PWM(Pin(25), frequencia) # objeto do led
  valor = (sensorValue - 32) * 255 // 4041 # transformando em numero de 8 bits
  led.duty(valor) # acionando o led
