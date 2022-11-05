'''
Utilizando um botão de pressionar para controlar o estado de um led (ligado ou desligado)
'''

from machine import Pin, ADC

led = Pin(2, Pin.OUT) #criando objeto led onde ele é definido no pino 2
botao = Pin(13, Pin.IN) #criando objeto botao onde ele é definido no pino 13

while(True): #loop
    botao_pressionado = botao.value() #armazenando o valor se o botao está pressionado na variavel botao_pressionado
    if botao_pressionado == True:
        led.value(1) #ligando o led
    else:           
        led.value(0) #desligando o led