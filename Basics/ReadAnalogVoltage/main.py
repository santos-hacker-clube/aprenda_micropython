'''
Este exemplo aplica-se ao ESP8266, que só pode receber no máximo 1V
na entrada ADC
'''
from machine import ADC
from time import sleep

# cria objeto referente a pino AD0 do Nodemcu ESP8266
pot = ADC(0)

while True:
    #realiza a leitura
	pot_value = pot.read()
	#exibe no shell o valor lido
	#utiliza 10bits para realizar a conversao 0 = 0V e 1024 = 1V
	print(pot_value)
	#pausa de 0.1 ms
	sleep(0.1)
