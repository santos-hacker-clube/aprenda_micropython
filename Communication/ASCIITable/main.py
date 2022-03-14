'''
Este que exibe no Shell caracteres
'''
#Os codigos ascii visiveis vao de 33 (!) ao 126 (~)
for ascii_code in range(33, 127):
    caracter = chr(ascii_code) #converte o cod de int para o caracter correspondente
    decimal = str(ascii_code) #converte o cod de int para String para ser exibido
    hexa = str(hex(ascii_code)) #converte o cod de int para hex e depois String
    octal = str(oct(ascii_code)) #converte o cod de int para octal e depois String
    binario =  str(bin(ascii_code)) #converte o cod de int para binario e depois String
    print(caracter+", dec: "+decimal+", hex: "+hexa+", oct: "+octal+", bin: "+binario)