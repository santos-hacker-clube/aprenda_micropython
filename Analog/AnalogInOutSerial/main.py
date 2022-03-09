""" Lê um valor (0-4095) de uma entrada analógica no pino 35 (potenciometro) e usa para uma saída PWM no pino
25 (led), convertendo o valor para tal (0-1023) """

from machine import Pin, ADC, PWM
import time

SENSORANALOGINPINNUM = 35 # pino de entrada
SENSORANALOGOUTPINNUM = 25 # pino de saída

def loop():
  inPin = Pin(SENSORANALOGINPINNUM, Pin.IN) # objeto do pino 35
  ADCInPin = ADC(inPin) # objeto ADC do pino 35
  value = ADCInPin.read() # leitura da entrada
  ledPin = Pin(SENSORANALOGOUTPINNUM, Pin.OUT) # objeto do pino 25
  duty = int(value // (4095 / 1023)) # adaptando o range do led
  PwmLedPin = PWM(ledPin, freq=5000, duty=duty) # objeto PWM do pino 25
  time.sleep(0.002) # tempo entre as leituras/loops (2 ms)
  PwmLedPin.deinit() # desliga a PWM do pino 25

while True:
  loop()

