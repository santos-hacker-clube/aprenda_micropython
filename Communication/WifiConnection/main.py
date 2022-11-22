#iniciamos um socket do tipo TCP 
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#vinculamos o socket a um endereço em branco é o ip do ESP na porta 80
s.bind(('', 80))

#escutamos no maximo 5 dispositivos
s.listen(5)

#fica rodando para o cliente se conectar
while True:
    #quando um cliente tenta se conectar ele aceita e retorna um objeto 
    conn, addr = s.accept()
    
    print('Esta conectado %s' % str(addr))
    #recebe o comando do cliente
    request = conn.recv(1024)
    request = str(request)
  
    
    print('Content = %s' % request)
    
    #inverte o valor do led
    led.value(not led.value())
    #Envia para o cliente o comando que foi recebido
    conn.send("O Comando "+ request+" de "+ addr[0]  +" foi recebido \n")
    #fecha a conexao
    conn.close()