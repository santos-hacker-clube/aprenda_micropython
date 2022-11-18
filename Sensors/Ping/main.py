"""
  Detectando objetos e sua respectiva distância com o sensor ultrassônico HC-SR04.
"""
from hcsr04 import HCSR04 # importando o código da biblioteca do sensor HC-SR04
from time import sleep # importando função sleep da biblioteca padrão timer

sensor = HCSR04(trigger_pin=18, echo_pin=5, echo_timeout_us=10000) # criando do sensor, definindo o pino do trigger na porta 15
                                                                   # o pino echo na porta 5 e a o tempo em milissegundos para poder
                                                                   # ouvir o pino de echo, o tempo padrão dessa variável é de 30000ms
while True: # loop
    distanciaCm = sensor.distance_cm() # armazenando a distância do objeto em centímetros. Utilizando a função distance_cm disponível no objeto sensor.
    print('Distancia:', distanciaCm, 'cm') # exibindo distância armazenada
    sleep(1) # aguardando 1 segundo até recomeçar o loop