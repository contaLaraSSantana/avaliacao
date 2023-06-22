# Aluno: Lara de S.Santana - Questão: "Procurando palavras na diagonal principal"


#Informações importantes:

    #ENTRADA

# N representa a quantidade de palavras que iremos verificar se existem no
# jogo limitado por [1,100]

#CADA PALAVRA N segue o limite de [6,100]

# M é a quantidade de linhas da matriz, limitado por [10,1000]

# P que representa a quantidade de colunas da *matriz* , limitado também por [10,1000]

    #SAÍDA

# Conforme a existencia de cada palavra N informe:
#1 palavra x na diagonal principal
#2 palavra x acima da diagonal principal
#3 palavra x abaixo da diagonal principal
#4 palavra X inexistente

# Eu realmente não sei se eu devo criar  a estrutura do jogo com as palavras prontas ou
# fazer um input pra isso, ja que elas seguem um limite de [6,100], não tem como eu criar
# tantas palavras.

PalavraN = ['workshop','videogame','scanner','computer','programation','scrumMethode','PowerBag']

M = int(input('Digite a quantidade de linhas da matriz: '))
#aqui de alguma forma eu preciso limitar por [10,1000]

P = int(input('Digite a quantidade de colunas da matriz: '))
#aqui de alguma forma eu preciso limitar por [10,1000]

# A partir dessas informações eu teria que fazer a matriz

N = int(input('Digite a quantidade de palavras que iremos verificar se existem no jogo: '))
#aqui de alguma forma eu preciso limitar por [1,100]

entrada = (input('Digite as palavras que quer verificar se existem no jogo: '))
#essas palavras, eu teria q jogar em uma lista ou tupla pra eu fazer a verificação por posições

#Ai eu faço uma estrutura de repetição que lê cada palavra da tupla PalavraN e verifica
# se alguma é igual a entrada, um detalhe é q eu teria q colocar para aceitar de trás
# pra frente, independente de qual tipo de letra é usado e também teriaa que mostrar a
# posição, mas pra isso eu precisaria da matriz que eu nao fiz :(

for n in range(PalavraN):
    if entrada == PalavraN.index:
        print([1], "Palavra existente na posição x")
        # posição da palavra de exemplo
        # x seria a posição que a palavra estaria na matriz criada

    else:
        print([1], "-Palavra inexistente")
        # posição da palavra de exemplo

# a questão principal da questão é a matriz por que o certo era eu em uma linha só ver
# o N, o M e o P. Depois coloca as palavras seguidas pra verificar. Eu iria percorrer a
# matriz e ir procurando linha pro linha das palavras exemplificadas. SE achar isola a posição
# tipo x e y (como eu faço isso eu ja não sei) e eu teria que fazer a comparação.
# o problema é para criar as letras de acordo com a escolha do jogador. Eu não sei como
#criar essas letras aletoriamente.
