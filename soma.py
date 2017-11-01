import numpy as np
import math

import decimal
decimal.getcontext().prec = 100

def autovalor(file):
    valr=file.readline().strip()	
    return valr
def opens(arquivo,tamanho,variancia):
    file = open("auto{}{}-{}.txt".format(arquivo,tamanho,variancia), "r")
    return file
def myexp(x):
    e=0
    pres=0.0001
    s=1
    i=1
    while s>pres:
        e=e+s
        s=(x**i)/math.factorial(i)
        i=i+1
    return e

def calculate(t,ta,n):
    numerador=decimal.Decimal(0)
    denominador=decimal.Decimal(0)
    exps=decimal.Decimal(0)
    file=opens('gaussian',ta,n)
    file2=opens('gaussian',ta,n)
    linhas=sum(1 for line in file)
    for a in range(linhas):
        lambdas=decimal.Decimal(autovalor(file2))
        pot=2*t*lambdas
        if pot>=700:
            pot1=700
            pot2=pot-700
            exps =decimal.Decimal(math.exp(pot1))*decimal.Decimal(math.exp(pot2))
        else:
            exps=decimal.Decimal(math.exp(pot))
        numerador=numerador+lambdas*exps
        denominador=denominador+exps
    frac=numerador/denominador
    return frac


def escrever(ta,arquivo,txt):

    file = open('resultadofinal{}-{}.dat'.format(ta,arquivo), 'w')
    file.write(txt)
    file.close()

def calcular(n,ta):
    txt=""
    for t in range(1,200):
        number=-calculate(t,ta,n)
        txt=txt+str(number)+"\n"
    escrever(ta,n,txt)

calcular(1,1000)
calcular(2,1000)
calcular(3,1000)
calcular(4,1000)
calcular(5,1000)


