import numpy as np
import math
#abre o arquivo de texto com dados
#define algumas variaveis vazias
arquivo='gaussian'
tamanho='1000'
variancia='-5'

file = open("{}{}{}.txt".format(arquivo,tamanho,variancia), "r") 
i=0
j=0
matrix=[]
#ve quantos dados tem no arquivo
num_lines = sum(1 for line in file)+1
#abre denovo, pq ja lemos todas as linhas
file = open("{}{}{}.txt".format(arquivo,tamanho,variancia), "r") 
#verifica quantas colunas a matrix vai ter (i) 
#:: obs:: j é o numero de dados, ele não pode passar o numero de linhas 
while j<=num_lines:
    i=i+1
    j=i+j
j=j-i
i=i-1
print("( matrix: {} dados lidos:{})".format(i,j))
## cria a matrix triangular, i-1 para garantir que vai ter a maior matrix possivel sem zeros, e normalizada
for a in range(i):
    matrix.append([])
    for b in range(i):
        if b<a:
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
symem= beginm + beginm.T
print("Pronto!!")
print("calculando auto valores da simetrica")
auto=np.linalg.eigvalsh(symem)
print("tudo feito e salvando em .txt")
np.savetxt("{}{}{}resul.txt".format(arquivo,tamanho,variancia), beginm, fmt="%f")
print("{}{}{}resul.txt salvo".format(arquivo,tamanho,variancia))
np.savetxt("{}{}{}sym.txt".format(arquivo,tamanho,variancia), symem, fmt="%f")
print("{}{}{}sym.txt salvo".format(arquivo,tamanho,variancia))
np.savetxt("auto{}{}{}.txt".format(arquivo,tamanho,variancia), auto, fmt="%f")

print("auto{}{}{}.txt salvo!!".format(arquivo,tamanho,variancia))
