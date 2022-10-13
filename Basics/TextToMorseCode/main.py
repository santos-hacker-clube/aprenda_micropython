'''
Transforma uma palavra em codigo morse com um buzzer
'''

from machine import Pin, PWM
from time import sleep


def beap(palavra, velocidade=100):

    # Criar um dicionario de listas contendo o tempo de cada letra deve apitar em Codigo Morse
    letras = {
        'a': [0.08, 0.24],
        'b': [0.24, 0.08, 0.08, 0.08],
        'c': [0.24, 0.08, 0.24, 0.08],
        'd': [0.24, 0.08, 0.08],
        'e': [0.08],
        'f': [0.08, 0.08, 0.24, 0.08],
        'g': [0.24, 0.24, 0.08],
        'h': [0.08, 0.08, 0.08, 0.08],
        'i': [0.08, 0.08],
        'j': [0.08, 0.24, 0.24, 0.24],
        'k': [0.24, 0.08, 0.24],
        'l': [0.08, 0.24, 0.08, 0.08],
        'm': [0.24, 0.24],
        'n': [0.24, 0.08],
        'o': [0.24, 0.24, 0.24],
        'p': [0.08, 0.24, 0.24, 0.08],
        'q': [0.24, 0.24, 0.08, 0.24],
        'r': [0.08, 0.24, 0.08],
        's': [0.08, 0.08, 0.08],
        't': [0.24],
        'u': [0.08, 0.08, 0.24],
        'v': [0.08, 0.08, 0.08, 0.24],
        'w': [0.08, 0.24, 0.24],
        'x': [0.24, 0.08, 0.08, 0.24],
        'y': [0.24, 0.08, 0.24, 0.24],
        'z': [0.24, 0.24, 0.08, 0.08]
    }
    velocidade = velocidade/100
    for letra in palavra:
        letra = letra.lower()

        for i in letras[letra]:
            speaker.duty_u16(1)
            sleep(i*velocidade)
            speaker.duty_u16(0)
            sleep(0.2*velocidade)
        sleep(0.01)


# Cria o objeto pin2 que usa o pino 2 (led interno) como saída
pin2 = Pin(2, Pin.OUT)

# Cria um pino artificial analogico com um pino digital
speaker = PWM(pin2, duty_u16=0)


# Define a frequencia do beap
speaker.freq(450)


speaker.duty_u16(0)
'''
Tempos: 
Beap curto: 0.08
beap Longo: 0.24

Tempo entre os beaps: 0.2

tempo entre as letras: 0.01

tempo entre espaços: 0.38
'''

# Chama a funcao passando a palavra a ser convertida em codigo morse, segundo parametro pode ser passado para acelerar ou diminuir a velocidade
beap("Giovane")
sleep(0.38)
beap("Cristiano")
