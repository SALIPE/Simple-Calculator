print("**********Python Calculator**********\n")
'''Essecomentariofuncionouna branch'''


#Function plus for sum numbers
def soma():
    valoressomados=[]

    def adicionar():
        try:
            adicionandovalor = float(input("Type a value:"))
            valoressomados.append(adicionandovalor)
            print("These are your values: {}".format(valoressomados))
        except ValueError:
            print("Value error!")
            adicionar()

        maisvalor = input("Do you wanna sum more numbers?(Yes or No)")

        if maisvalor == "Yes" or maisvalor == "yes":
            adicionar()
        else:
            somatotal = sum(valoressomados)
            print("SUM:{}".format(somatotal))
    adicionar()
#function for subtraction
def subtracao():

    def tentativa():
        global adicionandovalor

        try:

            adicionandovalor=float(input("Type a value:"))

            def segundatentativa():
                global outrovalor
                try:
                    outrovalor = float(input("Type another value to multiply:"))
                except ValueError:
                    print("Value error!")
                    segundatentativa()

            segundatentativa()

        except ValueError:
            print("Value error!")
            tentativa()


    tentativa()

    sub= adicionandovalor - outrovalor
    print("Subtraction={}".format(sub))
#function for multiply
def multiplicacao():

    def tentativa():
        global adicionandovalor

        try:

            adicionandovalor=float(input("Type a value:"))

            def segundatentativa():
                global outrovalor
                try:
                    outrovalor=float(input("Type another value to multiply:"))
                except ValueError:
                    print("Value error!")
                    segundatentativa()

            segundatentativa()

        except ValueError:
            print("Value error!")
            tentativa()


    tentativa()

    sub= adicionandovalor * outrovalor
    print("Multiply={}".format(sub))
#function to share
def divisao():

    def tentativa():
        global adicionandovalor

        try:

            adicionandovalor=float(input("Type a value:"))

            def segundatentativa():
                global outrovalor
                try:
                    outrovalor=float(input("Type another value to share:"))
                except ValueError:
                    print("Value error!")
                    segundatentativa()

            segundatentativa()

        except ValueError:
            print("Value error!")
            tentativa()


    tentativa()

    sub= adicionandovalor / outrovalor
    print("Share={}".format(sub))
#function to permutation
def permutaçao():

    def tentativa():
        global adicionandovalor

        try:
            adicionandovalor=int(input("Type a value:"))
        except ValueError:
            print("Value error!")
            tentativa()


    tentativa()

    def fatorial(numero):
        resultado = 1
        for n in range(1, numero + 1):
            resultado *= n


        return resultado

    sub=fatorial(adicionandovalor)

    print("Factiorial={}".format(sub))



calculos=['1','2','3','4','5','6']
#menu de escolha
while True:
    print("\n\n1-Soma+\n"
          "2-Subtração-\n"
          "3-Multiplicaçao*\n"
          "4-Divisão/\n"
          "5-Permutaçao!\n"
          "6-Sair\n")
    escolherOpcao= input("Choose a option:")
    while escolherOpcao not in calculos:
        escolherOpcao = input("Choose a option:")

    if escolherOpcao=='1':

            soma()
    elif escolherOpcao=='2':

            subtracao()
    elif escolherOpcao=='3':

            multiplicacao()
    elif escolherOpcao=='4':

            divisao()
    elif escolherOpcao=='5':

            permutaçao()
    elif escolherOpcao == '6':
        print("Bye!")
        break




















