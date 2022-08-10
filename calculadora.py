
operacao = input("Digite qual operação deseja realizar: \n + - Adição \n - - Subtração \n*- Multiplicação \n/ - Divisão")

number_1 = int(input('Digite o primeiro número: '))
number_2 = int(input('Digite o segundo número: '))

if operacao == '+':
    print('{} + {} = '.format(number_1, number_2))
    print(number_1 + number_2)
elif operacao == '-':
    print('{} - {} = '.format(number_1, number_2))
    print(number_1 - number_2)
elif operacao == '*':
    print('{} * {} = '.format(number_1, number_2))
    print(number_1 * number_2)
elif operacao == '/':
    print('{} / {} = '.format(number_1, number_2))
    print(number_1 / number_2)
else:
    print("Voce tem que digitar um operador valido, de acordo com o menu apresentado, tente novamente!")








#Subtração



#Multiplicação



#Divisão

