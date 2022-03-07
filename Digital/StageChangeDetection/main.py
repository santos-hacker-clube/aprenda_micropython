""" StateChangeDetection, detecção de mudança de estado: ao mudar o estado do botão do switch (on/off),
é impresso na tela o seu novo estado e, a cada 4 mudanças para o estado ligado(on), o led é aceso."""


from machine import Pin, ADC
import time

LEDPINNUM = 2 # numero do pino do led da placa
SWITCHBUTTONPINNUM = 35 # numero da entrada do switch

buttonPushCounter = 0 # contador do botão do switch
lastButtonState = 0 # último estado do botão do switch

def loop():
  global lastButtonState, buttonPushCounter
  buttonState = 0 # estado atual do botão
  ledPin = Pin(LEDPINNUM, Pin.OUT) # objeto do pino do led
  switchButtonPin = Pin(SWITCHBUTTONPINNUM, Pin.IN) # objeto do pino do botão do switch
  adcSBP = ADC(switchButtonPin) # objeto ADC do botão do switch
  buttonState = adcSBP.read() # leitura do estado do botão do switch (on/off)
  if buttonState != lastButtonState:
    if buttonState == 4095: # ligado (on)
      buttonPushCounter += 1
      print("on! num of button pushes: " + str(buttonPushCounter))
    elif buttonState == 0: # desligado (off)
      print("off!")
    time.sleep(0.05) # para evitar bouncing
  lastButtonState = buttonState

  if buttonPushCounter % 4 == 0:
    ledPin.on()
  else:
    ledPin.off()

while True:
  loop()