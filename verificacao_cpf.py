def teste1(cpf):
    if len(cpf) == 11:
        return True
    else:
        return False

def teste2(cpf):
    verificacao = 0
    i = 0
    while i < 10:
        if verificacao == 0:
            j = i + 1
            while j < 11:
                if cpf[i] == cpf[j]:
                    j = j + 1
                else:
                    verificacao = 1
                    break
            i = i + 1
        else:
            break
    if verificacao == 0:
        return False
    else:
        return True

def teste3(cpf):
    try:
        verificador = 10 * int(cpf[0]) + 9 * int(cpf[1]) + 8 * int(cpf[2]) + 7 * int(cpf[3]) + 6 * int(
            cpf[4]) + 5 * int(cpf[5]) + 4 * int(cpf[6]) + 3 * int(cpf[7]) + 2 * int(cpf[8])
        verificador = (10 * verificador) % 11
        if verificador == int(cpf[9]):
            verificador = 11 * int(cpf[0]) + 10 * int(cpf[1]) + 9 * int(cpf[2]) + 8 * int(cpf[3]) + 7 * int(
                cpf[4]) + 6 * int(cpf[5]) + 5 * int(cpf[6]) + 4 * int(cpf[7]) + 3 * int(cpf[8]) + 2 * int(cpf[9])
            verificador = (10 * verificador) % 11
            if verificador == int(cpf[10]):
                return True
            else:
                return False
        else:
            return False
    except:
        print('Não foi possível validar o cpf')

def validacao_de_cpf(cpf):
    if teste1(cpf):
        print('passou no primeiro teste')
        if teste2(cpf):
            print('passou no segundo teste')
            if teste3(cpf):
                print('passou no terceiro teste')
                print('cpf válido')
                return True
            else:
                print('cpf inválido')
                return False
        else:
            print('cpf inválido')
            return False
    else:
        print('cpf inválido')
        return False