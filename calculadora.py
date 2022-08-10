#definir a função calculadora
def calculadora():

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

    #Add função de fazer novamente a calculadora
    again()
def again():
    calc_again = input("Usuario, você deseja realizar outro calculo ? \nDigite S para sim e N para não: ")

    if calc_again.upper() == 'S':
        calculadora()
    elif calc_again.upper() == 'N':
        print('Obrigado por utilizar o sistema, volte sempre!')
    else:
        again()

calculadora()

