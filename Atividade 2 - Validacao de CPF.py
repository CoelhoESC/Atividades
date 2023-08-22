CPF = ''
CPF_usuario = ''
CPF_novo = ''
Lista = []
Cont = 0
multi = 10
Digito = ''

print('|VALIDAÇÃO DE CPF|'.center(20))
while True:
    if CPF == '':
        CPF = input('Digite seu CPF para validação: ').strip().replace('.', '').replace('-', '')
        if not CPF.isnumeric():
            print(f'Por favor digite apenas números! {CPF}: ERRO!')
            CPF = ''
        elif len(CPF) > 11:
            print(f'Digite seu CPF corretamente! {CPF} tem {len(CPF)} números!')
            CPF = ''
        else:
            continue
    else:
        Lista.clear()
        for valor in CPF:
            valor = int(valor)
            Lista.append(valor)

        if len(Lista) == 11:
            CPF_usuario = CPF
            *Outra_lista, num1, num2 = Lista
            for valor in Outra_lista:
                valor = str(valor)
                CPF_novo += valor
            Lista.clear()

            while Cont < len(Outra_lista):
                Mult = Outra_lista[Cont] * multi
                Cont += 1
                multi -= 1
                Lista.append(Mult)

            Soma_Total = sum(Lista)
            Digito = 11 - (Soma_Total % 11)
            if Digito > 9:
                Digito = '0'
                CPF_novo += Digito
            else:
                Digito = str(Digito)
                CPF_novo += Digito

            CPF = CPF_novo
            CPF_novo = ''

        elif len(Lista) == 10:
            Cont = 0
            multi = 11
            Lista2 = []
            for valor in Lista:
                valor = str(valor)
                CPF_novo += valor

            while Cont < 10:
                Mult = Lista[Cont] * multi
                Cont += 1
                multi -= 1
                Lista2.append(Mult)

            Soma_Total = sum(Lista2)
            Digito = 11 - (Soma_Total % 11)
            if Digito > 9:
                Digito = '0'
                CPF_novo += Digito
            else:
                Digito = str(Digito)
                CPF_novo += Digito

            CPF_Organ = ''
            if CPF_novo == CPF_usuario:
                for indices, valor in enumerate(CPF_novo):
                    if indices == 2 or indices == 5:
                        CPF_Organ += valor
                        CPF_Organ += '.'
                    elif indices == 8:
                        CPF_Organ += valor
                        CPF_Organ += '-'
                    else:
                        CPF_Organ += valor
                print(f'Seu CPF: {CPF_Organ} está validado!')
                break
            else:
                if len(CPF_usuario) == 9:
                    for indices, valor in enumerate(CPF_novo):
                        if indices == 2 or indices == 5:
                            CPF_Organ += valor
                            CPF_Organ += '.'
                        elif indices == 8:
                            CPF_Organ += valor
                            CPF_Organ += '-'
                        else:
                            CPF_Organ += valor
                    print(f'Seu CPF: "{CPF_Organ}" com os digitos!')
                    break
                else:
                    print(f'Seu CPF: {CPF_usuario} é diferente do CPF validado: {CPF_novo}')
                    break

        else:
            Lista3 = []
            CPF_usuario = CPF
            for valor in Lista:
                valor = str(valor)
                CPF_novo += valor

            while Cont < len(Lista):
                Mult = Lista[Cont] * multi
                Cont += 1
                multi -= 1
                Lista3.append(Mult)

            Soma_Total = sum(Lista3)
            Digito = 11 - (Soma_Total % 11)
            if Digito > 9:
                Digito = '0'
                CPF_novo += Digito
            else:
                Digito = str(Digito)
                CPF_novo += Digito

            CPF = CPF_novo
            CPF_novo = ''
