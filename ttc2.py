import numpy as np
import math
#abre o arquivo de texto com dados
file = open("gaussian700-1.txt", "r") 
#define algumas variaveis vazias
i=0
j=0
matrix=[]
#ve quantos dados tem no arquivo
num_lines = sum(1 for line in file)+1
#abre denovo, pq ja lemos todas as linhas
file = open("gaussian1000-5.txt", "r") 
#verifica quantas colunas a matrix vai ter (i) 
#:: obs:: j e o numero de dados, ele nao pode passar o numero de linhas 
while j<=num_lines:
    i=i+1
    j=i+j
print (i,j)
## cria a matrix triangular, i-1 para garantir que vai ter a maior matrix possivel sem zeros, e normalizada
for a in range(i-1):
    matrix.append([])
    for b in range(i-1):
        if b>a:
            matrix[a].append(0)
        else:
            valr=file.readline().strip()	
            try:     	
                line=float(valr)/math.sqrt(i)
                matrix[a].append(line)
            except:
                print(valr)

#salva no formato de matrix e simetriza etc.......

print("criando matrix triangular superior pelos dados")
beginm=np.matrix(matrix)
print("feito!")
print("tornando a matrix simetrica")
symem = beginm + beginm.T
print("Pronto!!")
print("calculando auto valores da siemtrica")
auto=np.linalg.eigvalsh(symem)
print("tudo feito e salvando em .txt")
np.savetxt("gaussianesul.txt", beginm, fmt="%f")
print("gaussianesul.txt salvo")
np.savetxt("gaussiansym.txt", symem, fmt="%f")
print("gaussiansym.txt salvo")
np.savetxt("auto700-1.txt", auto, fmt="%f")

print("auto.txt salvo!!")

import numpy as np
import math
#abre o arquivo de texto com dados
file = open("gaussian700-2.txt", "r") 
#define algumas variaveis vazias
i=0
j=0
matrix=[]
#ve quantos dados tem no arquivo
num_lines = sum(1 for line in file)+1
#abre denovo, pq ja lemos todas as linhas
file = open("gaussian700-3.txt", "r") 
#verifica quantas colunas a matrix vai ter (i) 
#:: obs:: j e o numero de dados, ele nao pode passar o numero de linhas 
while j<=num_lines:
    i=i+1
    j=i**2
print (i,j)
## cria a matrix triangular, i-1 para garantir que vai ter a maior matrix possivel sem zeros, e normalizada
for a in range(i-1):
    matrix.append([])
    for b in range(i-1):
        if b>a:
            matrix[a].append(0)
        else:
            valr=file.readline().strip()	
            try:     	
                line=float(valr)/math.sqrt(i)
                    matrix[a].append(line)
            except:
                print(valr)

#salva no formato de matrix e simetriza etc.......

print("criando matrix triangular superior pelos dados")
beginm=np.matrix(matrix)
print("feito!")
print("tornando a matrix simetrica")
symem = np.tril(beginm) + np.tril(beginm, -1).T
print("Pronto!!")
print("calculando auto valores da siemtrica")
auto=np.linalg.eigvalsh(symem)
print("tudo feito e salvando em .txt")
np.savetxt("gaussianesul.txt", beginm, fmt="%f")
print("gaussianesul.txt salvo")
np.savetxt("gaussiansym.txt", symem, fmt="%f")
print("gaussiansym.txt salvo")
np.savetxt("auto700-2.txt", auto, fmt="%f")

print("auto.txt salvo!!")

import numpy as np
import math
#abre o arquivo de texto com dados
file = open("gaussian700-3.txt", "r") 
#define algumas variaveis vazias
i=0
j=0
matrix=[]
#ve quantos dados tem no arquivo
num_lines = sum(1 for line in file)+1
#abre denovo, pq ja lemos todas as linhas
file = open("gaussian700-3.txt", "r") 
#verifica quantas colunas a matrix vai ter (i) 
#:: obs:: j e o numero de dados, ele nao pode passar o numero de linhas 
while j<=num_lines:
    i=i+1
    j=i**2
print (i,j)
## cria a matrix triangular, i-1 para garantir que vai ter a maior matrix possivel sem zeros, e normalizada
for a in range(i-1):
    matrix.append([])
    for b in range(i-1):
        if b>a:
            matrix[a].append(0)
        else:
            valr=file.readline().strip()	
                try:     	
                    line=float(valr)/math.sqrt(i)
                        matrix[a].append(line)
                except:
                    print(valr)

#salva no formato de matrix e simetriza etc.......

print("criando matrix triangular superior pelos dados")
beginm=np.matrix(matrix)
print("feito!")
print("tornando a matrix simetrica")
symem = np.tril(beginm) + np.tril(beginm, -1).T
print("Pronto!!")
print("calculando auto valores da siemtrica")
auto=np.linalg.eigvalsh(symem)
print("tudo feito e salvando em .txt")
np.savetxt("gaussianesul.txt", beginm, fmt="%f")
print("gaussianesul.txt salvo")
np.savetxt("gaussiansym.txt", symem, fmt="%f")
print("gaussiansym.txt salvo")
np.savetxt("auto700-3.txt", auto, fmt="%f")

print("auto.txt salvo!!")

import numpy as np
import math
#abre o arquivo de texto com dados
file = open("gaussian700-4.txt", "r") 
#define algumas variaveis vazias
i=0
j=0
matrix=[]
#ve quantos dados tem no arquivo
num_lines = sum(1 for line in file)+1
#abre denovo, pq ja lemos todas as linhas
file = open("gaussian700-4.txt", "r") 
#verifica quantas colunas a matrix vai ter (i) 
#:: obs:: j e o numero de dados, ele nao pode passar o numero de linhas 
while j<=num_lines:
    i=i+1
    j=i**2
print (i,j)
## cria a matrix triangular, i-1 para garantir que vai ter a maior matrix possivel sem zeros, e normalizada
for a in range(i-1):
    matrix.append([])
    for b in range(i-1):
        if b>a:
            matrix[a].append(0)
        else:
            valr=file.readline().strip()	
                try:     	
                    line=float(valr)/math.sqrt(i)
                        matrix[a].append(line)
                except:
                    print(valr)

#salva no formato de matrix e simetriza etc.......

print("criando matrix triangular superior pelos dados")
beginm=np.matrix(matrix)
print("feito!")
print("tornando a matrix simetrica")
symem = np.tril(beginm) + np.tril(beginm, -1).T
print("Pronto!!")
print("calculando auto valores da siemtrica")
auto=np.linalg.eigvalsh(symem)
print("tudo feito e salvando em .txt")
np.savetxt("gaussianesul.txt", beginm, fmt="%f")
print("gaussianesul.txt salvo")
np.savetxt("gaussiansym.txt", symem, fmt="%f")
print("gaussiansym.txt salvo")
np.savetxt("auto700-4.txt", auto, fmt="%f")

print("auto.txt salvo!!")

import numpy as np
import math
#abre o arquivo de texto com dados
file = open("gaussian700-5.txt", "r") 
#define algumas variaveis vazias
i=0
j=0
matrix=[]
#ve quantos dados tem no arquivo
num_lines = sum(1 for line in file)+1
#abre denovo, pq ja lemos todas as linhas
file = open("gaussian700-5.txt", "r") 
#verifica quantas colunas a matrix vai ter (i) 
#:: obs:: j e o numero de dados, ele nao pode passar o numero de linhas 
while j<=num_lines:
    i=i+1
    j=i**2
print (i,j)
## cria a matrix triangular, i-1 para garantir que vai ter a maior matrix possivel sem zeros, e normalizada
for a in range(i-1):
    matrix.append([])
    for b in range(i-1):
        if b>a:
            matrix[a].append(0)
        else:
            valr=file.readline().strip()	
                try:     	
                    line=float(valr)/math.sqrt(i)
                        matrix[a].append(line)
                except:
                    print(valr)

#salva no formato de matrix e simetriza etc.......

print("criando matrix triangular superior pelos dados")
beginm=np.matrix(matrix)
print("feito!")
print("tornando a matrix simetrica")
symem = np.tril(beginm) + np.tril(beginm, -1).T
print("Pronto!!")
print("calculando auto valores da siemtrica")
auto=np.linalg.eigvalsh(symem)
print("tudo feito e salvando em .txt")
np.savetxt("gaussianesul.txt", beginm, fmt="%f")
print("gaussianesul.txt salvo")
np.savetxt("gaussiansym.txt", symem, fmt="%f")
print("gaussiansym.txt salvo")
np.savetxt("auto700-5.txt", auto, fmt="%f")

print("auto.txt salvo!!")

import numpy as np
import math
#abre o arquivo de texto com dados
file = open("gaussian700-6.txt", "r") 
#define algumas variaveis vazias
i=0
j=0
matrix=[]
#ve quantos dados tem no arquivo
num_lines = sum(1 for line in file)+1
#abre denovo, pq ja lemos todas as linhas
file = open("gaussian700-6.txt", "r") 
#verifica quantas colunas a matrix vai ter (i) 
#:: obs:: j e o numero de dados, ele nao pode passar o numero de linhas 
while j<=num_lines:
    i=i+1
    j=i**2
print (i,j)
## cria a matrix triangular, i-1 para garantir que vai ter a maior matrix possivel sem zeros, e normalizada
for a in range(i-1):
    matrix.append([])
    for b in range(i-1):
        if b>a:
            matrix[a].append(0)
        else:
            valr=file.readline().strip()	
                try:     	
                    line=float(valr)/math.sqrt(i)
                        matrix[a].append(line)
                except:
                    print(valr)

#salva no formato de matrix e simetriza etc.......

print("criando matrix triangular superior pelos dados")
beginm=np.matrix(matrix)
print("feito!")
print("tornando a matrix simetrica")
symem = np.tril(beginm) + np.tril(beginm, -1).T
print("Pronto!!")
print("calculando auto valores da siemtrica")
auto=np.linalg.eigvalsh(symem)
print("tudo feito e salvando em .txt")
np.savetxt("gaussianesul.txt", beginm, fmt="%f")
print("gaussianesul.txt salvo")
np.savetxt("gaussiansym.txt", symem, fmt="%f")
print("gaussiansym.txt salvo")
np.savetxt("auto700-6.txt", auto, fmt="%f")

print("auto.txt salvo!!")

import numpy as np
import math
#abre o arquivo de texto com dados
file = open("gaussian700-7.txt", "r") 
#define algumas variaveis vazias
i=0
j=0
matrix=[]
#ve quantos dados tem no arquivo
num_lines = sum(1 for line in file)+1
#abre denovo, pq ja lemos todas as linhas
file = open("gaussian700-7.txt", "r") 
#verifica quantas colunas a matrix vai ter (i) 
#:: obs:: j e o numero de dados, ele nao pode passar o numero de linhas 
while j<=num_lines:
    i=i+1
    j=i**2
print (i,j)
## cria a matrix triangular, i-1 para garantir que vai ter a maior matrix possivel sem zeros, e normalizada
for a in range(i-1):
    matrix.append([])
    for b in range(i-1):
        if b>a:
            matrix[a].append(0)
        else:
            valr=file.readline().strip()	
                try:     	
                    line=float(valr)/math.sqrt(i)
                        matrix[a].append(line)
                except:
                    print(valr)

#salva no formato de matrix e simetriza etc.......

print("criando matrix triangular superior pelos dados")
beginm=np.matrix(matrix)
print("feito!")
print("tornando a matrix simetrica")
symem = np.tril(beginm) + np.tril(beginm, -1).T
print("Pronto!!")
print("calculando auto valores da siemtrica")
auto=np.linalg.eigvalsh(symem)
print("tudo feito e salvando em .txt")
np.savetxt("gaussianesul.txt", beginm, fmt="%f")
print("gaussianesul.txt salvo")
np.savetxt("gaussiansym.txt", symem, fmt="%f")
print("gaussiansym.txt salvo")
np.savetxt("auto700-7.txt", auto, fmt="%f")

print("auto.txt salvo!!")

import numpy as np
import math
#abre o arquivo de texto com dados
file = open("gaussian700-8.txt", "r") 
#define algumas variaveis vazias
i=0
j=0
matrix=[]
#ve quantos dados tem no arquivo
num_lines = sum(1 for line in file)+1
#abre denovo, pq ja lemos todas as linhas
file = open("gaussian700-8.txt", "r") 
#verifica quantas colunas a matrix vai ter (i) 
#:: obs:: j e o numero de dados, ele nao pode passar o numero de linhas 
while j<=num_lines:
    i=i+1
    j=i**2
print (i,j)
## cria a matrix triangular, i-1 para garantir que vai ter a maior matrix possivel sem zeros, e normalizada
for a in range(i-1):
    matrix.append([])
    for b in range(i-1):
        if b>a:
            matrix[a].append(0)
        else:
            valr=file.readline().strip()	
                try:     	
                    line=float(valr)/math.sqrt(i)
                        matrix[a].append(line)
                except:
                    print(valr)

#salva no formato de matrix e simetriza etc.......

print("criando matrix triangular superior pelos dados")
beginm=np.matrix(matrix)
print("feito!")
print("tornando a matrix simetrica")
symem = np.tril(beginm) + np.tril(beginm, -1).T
print("Pronto!!")
print("calculando auto valores da siemtrica")
auto=np.linalg.eigvalsh(symem)
print("tudo feito e salvando em .txt")
np.savetxt("gaussianesul.txt", beginm, fmt="%f")
print("gaussianesul.txt salvo")
np.savetxt("gaussiansym.txt", symem, fmt="%f")
print("gaussiansym.txt salvo")
np.savetxt("auto700-8.txt", auto, fmt="%f")

print("auto.txt salvo!!")

import numpy as np
import math
#abre o arquivo de texto com dados
file = open("gaussian700-9.txt", "r") 
#define algumas variaveis vazias
i=0
j=0
matrix=[]
#ve quantos dados tem no arquivo
num_lines = sum(1 for line in file)+1
#abre denovo, pq ja lemos todas as linhas
file = open("gaussian700-9.txt", "r") 
#verifica quantas colunas a matrix vai ter (i) 
#:: obs:: j e o numero de dados, ele nao pode passar o numero de linhas 
while j<=num_lines:
    i=i+1
    j=i**2
print (i,j)
## cria a matrix triangular, i-1 para garantir que vai ter a maior matrix possivel sem zeros, e normalizada
for a in range(i-1):
    matrix.append([])
    for b in range(i-1):
        if b>a:
            matrix[a].append(0)
        else:
            valr=file.readline().strip()	
                try:     	
                    line=float(valr)/math.sqrt(i)
                        matrix[a].append(line)
                except:
                    print(valr)

#salva no formato de matrix e simetriza etc.......

print("criando matrix triangular superior pelos dados")
beginm=np.matrix(matrix)
print("feito!")
print("tornando a matrix simetrica")
symem = np.tril(beginm) + np.tril(beginm, -1).T
print("Pronto!!")
print("calculando auto valores da siemtrica")
auto=np.linalg.eigvalsh(symem)
print("tudo feito e salvando em .txt")
np.savetxt("gaussianesul.txt", beginm, fmt="%f")
print("gaussianesul.txt salvo")
np.savetxt("gaussiansym.txt", symem, fmt="%f")
print("gaussiansym.txt salvo")
np.savetxt("auto700-9.txt", auto, fmt="%f")

print("auto.txt salvo!!")

import numpy as np
import math
#abre o arquivo de texto com dados
file = open("gaussian700-10.txt", "r") 
#define algumas variaveis vazias
i=0
j=0
matrix=[]
#ve quantos dados tem no arquivo
num_lines = sum(1 for line in file)+1
#abre denovo, pq ja lemos todas as linhas
file = open("gaussian700-10.txt", "r") 
#verifica quantas colunas a matrix vai ter (i) 
#:: obs:: j e o numero de dados, ele nao pode passar o numero de linhas 
while j<=num_lines:
    i=i+1
    j=i**2
print (i,j)
## cria a matrix triangular, i-1 para garantir que vai ter a maior matrix possivel sem zeros, e normalizada
for a in range(i-1):
    matrix.append([])
    for b in range(i-1):
        if b>a:
            matrix[a].append(0)
        else:
            valr=file.readline().strip()	
                try:     	
                    line=float(valr)/math.sqrt(i)
                        matrix[a].append(line)
                except:
                    print(valr)

#salva no formato de matrix e simetriza etc.......

print("criando matrix triangular superior pelos dados")
beginm=np.matrix(matrix)
print("feito!")
print("tornando a matrix simetrica")
symem = np.tril(beginm) + np.tril(beginm, -1).T
print("Pronto!!")
print("calculando auto valores da siemtrica")
auto=np.linalg.eigvalsh(symem)
print("tudo feito e salvando em .txt")
np.savetxt("gaussianesul.txt", beginm, fmt="%f")
print("gaussianesul.txt salvo")
np.savetxt("gaussiansym.txt", symem, fmt="%f")
print("gaussiansym.txt salvo")
np.savetxt("auto700-10.txt", auto, fmt="%f")

print("auto.txt salvo!!")

import numpy as np
import math
#abre o arquivo de texto com dados
file = open("gaussian700-11.txt", "r") 
#define algumas variaveis vazias
i=0
j=0
matrix=[]
#ve quantos dados tem no arquivo
num_lines = sum(1 for line in file)+1
#abre denovo, pq ja lemos todas as linhas
file = open("gaussian700-11.txt", "r") 
#verifica quantas colunas a matrix vai ter (i) 
#:: obs:: j e o numero de dados, ele nao pode passar o numero de linhas 
while j<=num_lines:
    i=i+1
    j=i**2
print (i,j)
## cria a matrix triangular, i-1 para garantir que vai ter a maior matrix possivel sem zeros, e normalizada
for a in range(i-1):
    matrix.append([])
    for b in range(i-1):
        if b>a:
            matrix[a].append(0)
        else:
            valr=file.readline().strip()	
                try:     	
                    line=float(valr)/math.sqrt(i)
                        matrix[a].append(line)
                except:
                    print(valr)

#salva no formato de matrix e simetriza etc.......

print("criando matrix triangular superior pelos dados")
beginm=np.matrix(matrix)
print("feito!")
print("tornando a matrix simetrica")
symem = np.tril(beginm) + np.tril(beginm, -1).T
print("Pronto!!")
print("calculando auto valores da siemtrica")
auto=np.linalg.eigvalsh(symem)
print("tudo feito e salvando em .txt")
np.savetxt("gaussianesul.txt", beginm, fmt="%f")
print("gaussianesul.txt salvo")
np.savetxt("gaussiansym.txt", symem, fmt="%f")
print("gaussiansym.txt salvo")
np.savetxt("auto700-11.txt", auto, fmt="%f")

print("auto.txt salvo!!")

import numpy as np
import math
#abre o arquivo de texto com dados
file = open("gaussian700-12.txt", "r") 
#define algumas variaveis vazias
i=0
j=0
matrix=[]
#ve quantos dados tem no arquivo
num_lines = sum(1 for line in file)+1
#abre denovo, pq ja lemos todas as linhas
file = open("gaussian700-12.txt", "r") 
#verifica quantas colunas a matrix vai ter (i) 
#:: obs:: j e o numero de dados, ele nao pode passar o numero de linhas 
while j<=num_lines:
    i=i+1
    j=i**2
print (i,j)
## cria a matrix triangular, i-1 para garantir que vai ter a maior matrix possivel sem zeros, e normalizada
for a in range(i-1):
    matrix.append([])
    for b in range(i-1):
        if b>a:
            matrix[a].append(0)
        else:
            valr=file.readline().strip()	
                try:     	
                    line=float(valr)/math.sqrt(i)
                        matrix[a].append(line)
                except:
                    print(valr)

#salva no formato de matrix e simetriza etc.......

print("criando matrix triangular superior pelos dados")
beginm=np.matrix(matrix)
print("feito!")
print("tornando a matrix simetrica")
symem = np.tril(beginm) + np.tril(beginm, -1).T
print("Pronto!!")
print("calculando auto valores da siemtrica")
auto=np.linalg.eigvalsh(symem)
print("tudo feito e salvando em .txt")
np.savetxt("gaussianesul.txt", beginm, fmt="%f")
print("gaussianesul.txt salvo")
np.savetxt("gaussiansym.txt", symem, fmt="%f")
print("gaussiansym.txt salvo")
np.savetxt("auto700-12.txt", auto, fmt="%f")

print("auto.txt salvo!!")

import numpy as np
import math
#abre o arquivo de texto com dados
file = open("gaussian700-13.txt", "r") 
#define algumas variaveis vazias
i=0
j=0
matrix=[]
#ve quantos dados tem no arquivo
num_lines = sum(1 for line in file)+1
#abre denovo, pq ja lemos todas as linhas
file = open("gaussian700-13.txt", "r") 
#verifica quantas colunas a matrix vai ter (i) 
#:: obs:: j e o numero de dados, ele nao pode passar o numero de linhas 
while j<=num_lines:
    i=i+1
    j=i**2
print (i,j)
## cria a matrix triangular, i-1 para garantir que vai ter a maior matrix possivel sem zeros, e normalizada
for a in range(i-1):
    matrix.append([])
    for b in range(i-1):
        if b>a:
            matrix[a].append(0)
        else:
            valr=file.readline().strip()	
                try:     	
                    line=float(valr)/math.sqrt(i)
                        matrix[a].append(line)
                except:
                    print(valr)

#salva no formato de matrix e simetriza etc.......

print("criando matrix triangular superior pelos dados")
beginm=np.matrix(matrix)
print("feito!")
print("tornando a matrix simetrica")
symem = np.tril(beginm) + np.tril(beginm, -1).T
print("Pronto!!")
print("calculando auto valores da siemtrica")
auto=np.linalg.eigvalsh(symem)
print("tudo feito e salvando em .txt")
np.savetxt("gaussianesul.txt", beginm, fmt="%f")
print("gaussianesul.txt salvo")
np.savetxt("gaussiansym.txt", symem, fmt="%f")
print("gaussiansym.txt salvo")
np.savetxt("auto700-13.txt", auto, fmt="%f")

print("auto.txt salvo!!")

import numpy as np
import math
#abre o arquivo de texto com dados
file = open("gaussian700-14.txt", "r") 
#define algumas variaveis vazias
i=0
j=0
matrix=[]
#ve quantos dados tem no arquivo
num_lines = sum(1 for line in file)+1
#abre denovo, pq ja lemos todas as linhas
file = open("gaussian700-14.txt", "r") 
#verifica quantas colunas a matrix vai ter (i) 
#:: obs:: j e o numero de dados, ele nao pode passar o numero de linhas 
while j<=num_lines:
    i=i+1
    j=i**2
print (i,j)
## cria a matrix triangular, i-1 para garantir que vai ter a maior matrix possivel sem zeros, e normalizada
for a in range(i-1):
    matrix.append([])
    for b in range(i-1):
        if b>a:
            matrix[a].append(0)
        else:
            valr=file.readline().strip()	
                try:     	
                    line=float(valr)/math.sqrt(i)
                        matrix[a].append(line)
                except:
                    print(valr)

#salva no formato de matrix e simetriza etc.......

print("criando matrix triangular superior pelos dados")
beginm=np.matrix(matrix)
print("feito!")
print("tornando a matrix simetrica")
symem = np.tril(beginm) + np.tril(beginm, -1).T
print("Pronto!!")
print("calculando auto valores da siemtrica")
auto=np.linalg.eigvalsh(symem)
print("tudo feito e salvando em .txt")
np.savetxt("gaussianesul.txt", beginm, fmt="%f")
print("gaussianesul.txt salvo")
np.savetxt("gaussiansym.txt", symem, fmt="%f")
print("gaussiansym.txt salvo")
np.savetxt("auto700-14.txt", auto, fmt="%f")

print("auto.txt salvo!!")

import numpy as np
import math
#abre o arquivo de texto com dados
file = open("gaussian700-15.txt", "r") 
#define algumas variaveis vazias
i=0
j=0
matrix=[]
#ve quantos dados tem no arquivo
num_lines = sum(1 for line in file)+1
#abre denovo, pq ja lemos todas as linhas
file = open("gaussian700-15.txt", "r") 
#verifica quantas colunas a matrix vai ter (i) 
#:: obs:: j e o numero de dados, ele nao pode passar o numero de linhas 
while j<=num_lines:
    i=i+1
    j=i**2
print (i,j)
## cria a matrix triangular, i-1 para garantir que vai ter a maior matrix possivel sem zeros, e normalizada
for a in range(i-1):
    matrix.append([])
    for b in range(i-1):
        if b>a:
            matrix[a].append(0)
        else:
            valr=file.readline().strip()	
                try:     	
                    line=float(valr)/math.sqrt(i)
                        matrix[a].append(line)
                except:
                    print(valr)

#salva no formato de matrix e simetriza etc.......

print("criando matrix triangular superior pelos dados")
beginm=np.matrix(matrix)
print("feito!")
print("tornando a matrix simetrica")
symem = np.tril(beginm) + np.tril(beginm, -1).T
print("Pronto!!")
print("calculando auto valores da siemtrica")
auto=np.linalg.eigvalsh(symem)
print("tudo feito e salvando em .txt")
np.savetxt("gaussianesul.txt", beginm, fmt="%f")
print("gaussianesul.txt salvo")
np.savetxt("gaussiansym.txt", symem, fmt="%f")
print("gaussiansym.txt salvo")
np.savetxt("auto700-15.txt", auto, fmt="%f")

print("auto.txt salvo!!")
