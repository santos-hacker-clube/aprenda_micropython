'''
Utiliza o led interno do esp (pin 2) para simular o fade usando PWM
O Esp não possui saída analógica, por tanto sem se utilizar o PMW
'''

import time, math, machine

# funcao para variar o duty cicle do PWM l é o led e t determina a velocidade do pisca
def pulse(l, t):
    for i in range(20):
        l.duty(int(math.sin(i/10 * math.pi)*500+500))
        time.sleep_ms(t)

# cria o objeto led vinculado ao pin 2 em modo pwm
# o parametro freq que definirá a intensidade
led = machine.PWM(machine.Pin(2), freq = 150)

# chama a funcao pulse 10 vezes
for i in range(10):
    pulse(led, 100)


