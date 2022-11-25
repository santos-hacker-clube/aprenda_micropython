#importa a biblioteca socket para a conexao com um dispositivo
import socket
#importa a biblioteca network para conectar ao wifi
import network

from machine import Pin
from time import sleep

#importa modulo gc para limpeza da memoria
import gc
#libera espaço excluindo objetos sem referencias 
gc.collect()


import esp
#desativa os logs no prompt
esp.osdebug(None)

#nome da rede
ssid = ''
#senha da rede
password = ''

#Classe Wlan recece o parametro para informar que será conectado em uma rede
station = network.WLAN(network.STA_IF)

#ativa o modulo wireless
station.active(True)
#conecta na rede
station.connect(ssid, password)

#Espera ate que tenha se conectado 
while station.isconnected() == False:
  pass

print('Connection successful')
#imprime as configuralções de Ip e pisca o led 3 vezes se a conexao foi bem sucedida
print(station.ifconfig())
led = Pin(2, Pin.OUT)
led.value(not led.value())
sleep(0.3)
led.value(not led.value())
sleep(0.3)
led.value(not led.value())
sleep(0.3)
led.value(not led.value())
sleep(0.3)
led.value(not led.value())
sleep(0.3)
led.value(not led.value())