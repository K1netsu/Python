from sys import argv

script, filename = argv

#Abre o arquivo para leitura e gravação
arquivo = open(filename, "r+")
print(arquivo.read())
#Move o ponteiro para o início do arquivo
arquivo.seek(0)
#Sobrescreve o arquivo com o seguinte texto:
arquivo.write("O carro agora e azul")
#Move o ponteiro para o início novamente para que ocorra a leitura do arquivo
arquivo.seek(0)
print(arquivo.read())
arquivo.close()