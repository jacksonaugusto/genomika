




modulos = '035 12 4 67'

carregamentos = modulos.split()

moduloscarregados = ''

for x in range(0,100):



        entrada = str(input('Digite o número do módulo para carregamento:'))
        num = int(entrada)
        if num > -1 and num < 8:

            if entrada == '0' or entrada == '1' or entrada == '4':
                moduloscarregados = moduloscarregados + entrada
                print('modulo', entrada ,'adicionado!')
                print('modulos carregados até o momento:', moduloscarregados)

            elif entrada == '6' and moduloscarregados.find('2') == -1 and moduloscarregados.find(
                    '5') == -1 and moduloscarregados.find('4') == -1:
                print('faltam carregar os módulos 2,4 e 5')

            elif moduloscarregados.find('2') != -1 and moduloscarregados.find('5') != -1 and moduloscarregados.find('4') != -1:
                if entrada == '7' and moduloscarregados.find('5') != -1 and moduloscarregados.find('6') != -1:
                    moduloscarregados = moduloscarregados + entrada
                    print('modulo', entrada, 'adicionado!')
                    print('modulos carregados até o momento:', moduloscarregados)

                elif entrada == '7' and moduloscarregados.find('6') == -1:
                    print('faltam carregar o módulo:', 6)


                else:
                    moduloscarregados = moduloscarregados + entrada
                    print('modulo', entrada, 'adicionado!')
                    print('modulos carregados até o momento:', moduloscarregados)

            else:
                for c in range(0,3):
                    modulocomp = carregamentos[c]
                    for i in range(0,len(carregamentos[c])):

                        if entrada == modulocomp[i] and moduloscarregados.find(modulocomp[0:i]) != -1:
                            moduloscarregados = moduloscarregados + entrada
                            print('modulo', entrada, 'adicionado!')
                            print('modulos carregados até o momento:', moduloscarregados)


                        elif entrada == modulocomp[i] or entrada == '7':
                            print('faltam carregar o módulo:', modulocomp[i - 1])

        else:
            print('Tente novamenete. Digite um número de 0 a 7 \n')