'''
Lê uma entrada digital recebida no pino 12 (D6 NodeMCU Lolin v3, verifique a sua placa),
vinda do pressionamento de um botão, e exibe se o botão foi pressionado no Shell.

Verifique as conexões no arquivo layout.png
'''

import machine
import time

#cria o objeto botao, vinculado a entrada do pino 12 em modo PULL_UP
botao = machine.Pin(12, machine.Pin.IN, machine.Pin.PULL_UP)

while True:
    #verifica o estado da entrada digital
    if not botao.value():
        print("Botao Pressionado")
    #aguarda 200ms para soltar o botão e dar estabilidade a leitura
    time.sleep(0.2)