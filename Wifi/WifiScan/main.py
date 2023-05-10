#importa a biblioteca network para escanear redes WiFi
import network

#importa a biblioteca time que contém a função sleep
import time

#define o WiFi para o modo estação (STA) (conexão à uma rede)
wlan = network.WLAN(network.STA_IF)
wlan.active(True)

#armazena os protocolos de segurança WiFi
protocolo = ['Open', 'WEP', 'WPA-PSK', 'WPA2-PSK4', 'WPA/WPA2-PSK']

#loop
while True:

  print("Escaneando redes WiFi, por favor aguarde...")
  print()

  #armazena os valores do scan, esse que retorna as redes encontradas
  redes = wlan.scan()

  #verifica quantas redes foram encontradas e imprime no console
  if (len(redes) == 0):
    print("Nenhuma rede encontrada.")
  else:
    print("{} {}".format(len(redes), "rede encontrada" if len(redes) == 1 else "redes encontradas"))

    print()

    #imprime o cabeçalho
    print ("Nr | SSID                             | RSSI | Canal | Segurança    | BSSID")

    #imprime as informações de cada rede escaneada
    for i, (ssid, bssid, channel, rssi, seguranca, hidden) in enumerate(redes):
      print("{:2d}".format(i+1), end=" | ")
      print("{:32s}".format(ssid), end=" | ")
      print("{:4d}".format(rssi), end=" | ")
      print("{:5d}".format(channel), end=" | ")
      print("{:12s}".format(protocolo[seguranca]), end=" | ")
      print("{:02x}:{:02x}:{:02x}:{:02x}:{:02x}:{:02x}".format(*bssid))

  print()

  #aguarda 3 segundos para escanear novamente
  time.sleep(3)
