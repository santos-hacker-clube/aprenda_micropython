""" Esse código mostra como deixar um led piscando, usando PWM para controlar
    a potência na saída digital 25
    autor: Gabriel Zamarioli Youssef
    data: 07/03/2022
"""


from machine import Pin, PWM
import time

LEDPINNUM = 25 # numero do pino do led

def loop():
  ledPin = Pin(LEDPINNUM, Pin.OUT) # objeto do pino 25
  for x in range(1,1024, 20): # indo de 1 a 1024, num passo +20 a cada 10 ms
    pwm = PWM(ledPin, freq=5000, duty=x) # objeto PWM do pino 25 (liga)
    time.sleep(0.01)
    pwm.deinit() # (desliga)
  for x in range(1023, 1, -20): # indo de 1024 a 1, num passo -20 a cada 10 ms
    pwm = PWM(ledPin, freq=5000, duty=x) # objeto PWM do pino 25 (liga)
    time.sleep(0.01)
    pwm.deinit() # (desliga)

while True:
  loop()