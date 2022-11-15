'''
Lê uma entrada digital recebida no pino 25 (ESP32, verifique a sua placa),
alterada com o pressionamento de um botão, e exibe o resultado no Shell.
Verifique as conexões no arquivo layout.png
'''

from machine import Pin
import time

#cria o objeto botao, vinculado a entrada do pino 25 em modo input
botao = Pin(25, Pin.IN)

while True:
    #exibe o estado da entrada digital
    print(botao.value())
    #aguarda 200ms para dar estabilidade a leitura
    time.sleep(0.2)
