#Função para calcular o IMC
def calcular_IMC(peso, altura):
     return peso / altura **2


#Função para fazer as interpretaçoes do IMC
def interpretar_IMC(imc):
    if imc < 18.5:
        return 'Abaixo do peso'
    elif 18.5 <= imc < 24.9:
        return 'Peso ideal'
    elif 25 <= imc < 29.9:
        return 'Sobrepeso'
    elif 30 <= imc < 34.9:
        return 'Obesidade Grau I'
    elif 35 <= imc < 39.9:
        return 'Obesidade Grau II'
    else:
        return 'Obesidade Grau II'
    
    #Pega os dados do prompt
try:
    peso = float(input('Digite seu peso (kg): '))
    altura = float(input('Digite sua altura (m): '))
except ValueError:
    print('Por favor, insira solo numeros válidos para peso e altura.')
else:
    # Calcula o IMC
    imc = calcular_IMC(peso, altura)

    # Interpreta o IMC
    interpretacao = interpretar_IMC(imc)

    # Exibe o resultado
    print(f"Seu IMC é {imc:.2f}, o que significa que você está {interpretacao}.")