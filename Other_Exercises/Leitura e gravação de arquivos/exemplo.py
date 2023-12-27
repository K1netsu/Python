from sys import argv

script, nomeDoArquivo = argv

#Abre o arquivo para leitura e printa na tela a cor do carro.
arquivo = open(nomeDoArquivo, "r")
print(arquivo.read())

#Abre o arquivo para gravação e atribui a nova cor do carro.
arquivo = open(nomeDoArquivo, 'w')

#Não é necessário utilizar o .truncate() para efetuar a limpeza 
#do que está escrito nesse arquivo nesse exemplo pois o 'w' 
#já executa isso normalmente.
arquivo.write("O carro agora é azul\n")

#Abre o arquivo para leitura novamente, pois durante o modo 'w'
#não tem como haver a leitura do que há dentro do arquivo.
arquivo = open(nomeDoArquivo, 'r')
print(arquivo.read())

arquivo.close()
