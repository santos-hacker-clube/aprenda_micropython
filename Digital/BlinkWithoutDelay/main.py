'''
Este exemplo faz uso do tick_ms que recebe o valor em ms de um timer
do ESP. Definido um intervalo é feito um calculo da diferenca de tempo
entre o ultimo estado modificado do led
'''
from machine import Pin
import time

#cria o objeto led que usa o pino 2 (led interno) como saída
led = Pin(2,Pin.OUT)

#variavel que armazena o estado do led, inicialmente False
ledState = False

#variavel que armazena o tempo em que houve a ultima alteracao de estado
#inicialmente 0
previousMillis = 0

#variavel que define o intervalo de tempo entre a troca de um estado para o outro
#modifique aqui para deixar mais rapido ou devagar, intervalo em ms
interval = 1000

#loop infinito para sair pressione CTRL+C no interpretador shell
while True:
    #armazena a leitura atual do clock
    currentMillis = time.ticks_ms()
    
    #se a diferenca da leitura atual e a ultima vez em que houve a alteracao de estado
    #for maior ou igual ao intervalo establecido entra no if
    if (currentMillis - previousMillis) >= interval:
        #o tempo atual sera colocado na variavel previouMillis
        previousMillis = currentMillis
        
        #faz a alteracao de estado da variavel ledState
        if ledState:
            ledState = False
        else:
            ledState = True
            
        #modifica a saida do pin2, led interno
        led.value(ledState)    

