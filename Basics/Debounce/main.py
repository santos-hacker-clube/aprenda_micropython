""" Debounce lê a posição do botão do switch(pino 35) para ligar e desligar o led(pino 2),
    caso o tempo entre as mudanças foi maior que 5 ms """

from machine import Pin, ADC
import time

BUTTONPINNUM = 35 # pino 35 de entrada analógica
LEDPINNUM = 2 # pino do led da placa
ledState = 1 # estado do led (ligado)
lastDebounceTime = 0 # ultimo tempo de debounce
debounceDelay = 0.05 # tempo entre mudanças de estado (50 ms)
buttonState = 0 # estado do botão do switch
lastButtonState = 0 # ultimo estado do botão do switch

def setup(): # liga o led pela primeira vez
  ledPin = Pin(LEDPINNUM, Pin.OUT)
  ledPin.value(ledState)

def loop(): # desliga/liga o led se o botão do switch está no estado 1 e o tempo entre as mudanças > 0.50 ms
  while True:
    global lastButtonState, lastDebounceTime, ledState, buttonState
    start = time.ticks_ms() # começa a contar o tempo
    buttonPin = Pin(BUTTONPINNUM, Pin.IN) # objeto do botão do switch
    ledPin = Pin(LEDPINNUM, Pin.OUT) # objeto do led
    adc = ADC(buttonPin) # objeto ADC do botão do switch
    reading = adc.read() # lê o valor de entrada do botão do switch (0 ou 4095)

    if reading != lastButtonState: # caso o valor seja diferente do anterior
      lastDebounceTime = time.ticks_diff(time.ticks_ms(), start) # atualiza o ultimo tempo entre as entradas

    # se o tempo decorrido menos o ultimo(acima) é o suficiente (> 50 ms)
    if time.ticks_diff(time.ticks_ms(), start) - lastDebounceTime > debounceDelay: 
      if reading != buttonState: 
        buttonState = reading # muda o estado do botão do switch caso seja um novo valor (0 ou 4095)

        if buttonState == 4095: # a mudança só ocorre caso o botão d switch estiver na posição 4095(liga)
          ledState = 1 if (ledState == 0) else 0 # a mudança ocorre

    ledPin.value(ledState) # a mudança eh realizada
    lastButtonState = reading # atualiza o último estado do botão

setup()
loop()
