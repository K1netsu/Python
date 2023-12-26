def calcularResposta():
    print("O que você deseja converter, altura ou peso?")
    escolhaDoCalculo = input(("Digite: Altura para altura e Peso para peso - "),)
    escolhaDoCalculo = escolhaDoCalculo.lower()
    print("")
     
    if escolhaDoCalculo == 'altura':
            print("Escolha qual conversão você quer que seja feita:")
            print("1: Cm -> Ft")
            print("2: Ft -> Cm")
            print("")
            
            tipoDeConversão = input("Escreva 1 ou 2: ",)
            
            if tipoDeConversão == '1':
                print("")
                alturaEmCm = float(input("Digite a sua altura em centímetros: "))
                alturaConvertida = alturaEmCm / 30.48
                print("")
                print(f"A altura convertida é de {alturaConvertida:.2f} fts.")
                return alturaConvertida
            elif tipoDeConversão == '2':
                print("")
                alturaEmFt = float(input("Digite a sua altura em pés: "))
                alturaConvertida = alturaEmFt * 30.48
                print("")
                print(f"A altura convertida é de {alturaConvertida:.0f} cm.")
                return alturaConvertida
    elif escolhaDoCalculo == 'peso':
            print("Escolha qual conversão você quer que seja feita:")
            print("1: Kg -> Lb")
            print("2: Lb -> Kg")    
            print("")

            tipoDeConversão = input("Escreva 1 ou 2: ")
            
            if tipoDeConversão == '1':
                print("")
                pesoEmKg = float(input("Digite o seu peso em kilos: "))
                valorConvertido = pesoEmKg * 2.205
                print("")
                print(f"O seu peso convertido é de {valorConvertido:.2f} lbs.")
                return valorConvertido
            
            elif tipoDeConversão == '2':
                print("")
                pesoEmLb = float(input("Digite o seu peso em libras: "))
                valorConvertido = pesoEmLb / 2.205
                print("")
                print(f"O seu peso convertido é de {valorConvertido:.1f} kg.")   
                return valorConvertido
        
print ("Olá, bem vindo ao conversor de altura ou de peso!")
print ("Gostaria de converter? ")

#estipulando as possíveis respostas
possiveisRespostas = ['sim','s','não','n']

#loop feito para identificar as respostas positivas, negativas e as respostas que
#não foram dadas conforme o esperado
for resposta in possiveisRespostas:
    resposta = input("Escreva (Sim/Não) ou (S/N): ")
    resposta = resposta.lower() #feito para manter os resultados em minúsculo.
    print("")
    
    #caso a resposta seja sim ou s, haverá conversão.
    if resposta == possiveisRespostas[0] or resposta == possiveisRespostas[1]:
        #função feita para executar o cálculo a fim de reduzir o código.
        calcularResposta()
        break
    #caso a resposta seja não ou n, não haverá conversão.
    elif resposta == possiveisRespostas [2] or resposta == possiveisRespostas[3]:
        print("Okey, tenha um bom dia!")
        break
    #caso a resposta seja diferente do esperado, o usuário terá uma chance de 
    #escrever novamente a resposta conforme o que foi pedido.
    else:
        print("Digite corretamente conforme foi instruído.")
        continue
