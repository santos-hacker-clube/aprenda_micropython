'''
Esse exemplo demonstra o uso do Pin.PULL_UP utilizando o argumento pull
do construtor machine.Pin. Lê a entrada digital no pino 4 e exibe o resultado
no Shell, utilizando um LED que acende quando o botao é pressionado.
Diferente de apenas o argumento mode input declarado (Pin.IN) sem um pull
(None ou vazio), não é necessário um resistor pull-down externo. Um resistor
interno é definido para 3,3V, essa configuração faz a entrada ler HIGH quando
a chave está aberta, e LOW quando esta fechada.
Verifique as conexões no arquivo layout.png
'''

from machine import Pin
import time

#cria o objeto botao, vinculado a entrada do pino 4 em modo input e
#ativa o resistor pull-up interno
botao = Pin(4, Pin.IN, Pin.PULL_UP)
#cria o objeto led, vinculado a entrada do pino 13 em modo output
led = Pin(13, Pin.OUT)

while True:
    #coloca o valor do botao em uma variavel
    sensorVal = botao.value()
    #exibe o valor do botao
    print(sensorVal)
    
    #lembre-se que o pull-up significa que a logica do botao é invertida.
    #HIGH (1) quando a chave está aberta (botao solto) e LOW (0) quando
    #está fechada (botao pressionado). Ative o pino 13 quando o botao 
    #estiver pressionado e desative quando não estiver:
    if sensorVal:
        led.value(0)
    else:
        led.value(1)
    #aguarda 100ms para dar estabilidade a leitura
    time.sleep(0.1)
