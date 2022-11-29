from datetime import datetime
import time
def teste1(retirada, devolucao):
    if retirada < devolucao:
        print('passou no primeiro teste')
        return True
    else:
        return False

def teste2(retirada, devolucao, tempo):
    if devolucao - retirada < tempo:
        print('passou no segundo teste')
        return True
    else:
        return False

def testes(retirada, devoolucao, tempo):
    if teste1(retirada, devoolucao):
        if teste2(retirada, devoolucao, tempo):
            return True
        else:
            return False
    else:
        return False